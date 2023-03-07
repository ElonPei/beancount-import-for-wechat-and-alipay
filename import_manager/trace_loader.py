import os

import hashlib
import pandas as pd

import import_manager.formater_csv as fmt
from import_manager.beans_loader import load_custom_info

trade_path = '/Users/peiel/Desktop/123/'

wechat_header_pickers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alipay_header_pickers = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10]
alipay_header_pickers_v2 = [10, 7, 1, 3, 0, 5, 4, 6, 8, 9]

df_common_columns = ['date', 'trace_type', 'trace_obj', 'goods', 'income_and_expenses', 'amount', 'pay_way', 'status',
                     'order_no', 'business_order_no']


def filter_df(df):
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df.drop_duplicates(
        subset=['date', 'trace_type', 'trace_obj', 'goods', 'income_and_expenses', 'amount', 'pay_way'],
        keep='first', inplace=True)

    # 拼接日期和金额并计算md5值
    df['id'] = df.apply(lambda x: hashlib.md5((str(x['date']) + x['amount']).encode()).hexdigest(), axis=1)

    # 对原始文件中标记的内容进行处理
    df_remark = load_custom_info()
    df = pd.merge(df, df_remark, on='id', how='left')
    df.fillna("", inplace=True)

    # 对带双引号的数据进行替换处理
    df['trace_obj'] = df['trace_obj'].str.replace("\"", "'")
    df['goods'] = df['goods'].str.replace("\"", "'")

    return df


def format_amount(df):
    df['amount'] = df['amount'].str.replace("¥", '').astype(float)

    # 下列两种方式都没有生效，后续探究
    # df['amount']=df['amount'].apply(lambda x:round(x,2))
    # df['amount'] = round(df['amount'], 2)

    return df


def parse_owner(root):
    rep_root = root.replace(trade_path, '')
    if not rep_root:
        return 'default'
    return rep_root


def load_wechat_trace():
    df = pd.DataFrame()
    all_files = []
    for root, _, files in os.walk(trade_path):
        all_files = all_files + [root + '/' + f for f in files if 'csv' in f]

    for f in all_files:
        if '微信支付' not in f:
            continue
        inner_df = pd.DataFrame(fmt.format_wechat_to_list(f))
        inner_df.columns = inner_df.iloc[0]
        inner_df = inner_df[1:]

        inner_df = inner_df.iloc[:, wechat_header_pickers]
        inner_df.columns = df_common_columns
        inner_df['owner'] = '卢娇艳' if 'ljy' in f else '裴二龙'
        inner_df['source'] = f
        inner_df['file_update_time'] = os.stat(f).st_mtime
        df = pd.concat([df, inner_df])
    return df


def load_alipay_trace():
    df = pd.DataFrame()
    all_files = []
    for root, _, files in os.walk(trade_path):
        all_files = all_files + [root + '/' + f for f in files if 'csv' in f]
    for f in all_files:
        if 'alipay' not in f:
            continue
        inner_df = pd.DataFrame(fmt.format_alipay_to_list(f))

        # 把第一行当做表头并删除第一行
        inner_df.columns = inner_df.iloc[0]
        inner_df = inner_df[1:]

        # 如果是新版格式的导出，删除最后一列备注
        if inner_df.columns[0].strip() == '交易时间':
            # 使用 .drop() 方法删除最后一列
            inner_df.drop(inner_df.columns[-1], axis=1, inplace=True)

        # 判断新旧版本来使用不同的头部
        if inner_df.columns[0].strip() == '交易时间':
            inner_df = inner_df.iloc[:, alipay_header_pickers]
        if inner_df.columns[0].strip() == '收/支':
            inner_df = inner_df.iloc[:, alipay_header_pickers_v2]

        inner_df.columns = df_common_columns

        inner_df['owner'] = '卢娇艳' if 'ljy' in f else '裴二龙'
        inner_df['source'] = f
        inner_df['file_update_time'] = os.stat(f).st_mtime

        df = pd.concat([df, inner_df])

    return df


def load_all_trace():
    df = pd.concat([load_wechat_trace(), load_alipay_trace()])

    if df.empty:
        return df

    df = filter_df(df)
    df = format_amount(df)

    df = df.sort_values(by=['date', 'file_update_time'])
    return df


if __name__ == '__main__':
    all_df = load_all_trace()
    print(len(all_df))
    print(all_df.head())
