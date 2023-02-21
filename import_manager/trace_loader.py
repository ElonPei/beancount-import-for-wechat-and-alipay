import os

import hashlib
import pandas as pd

import import_manager.formater_csv as fmt
from import_manager.beans_loader import load_remark_info
from import_manager.trace_filter import delete_not_use_trace

trade_path = '/Users/peiel/Desktop/123/'


def sort_by_trace_time(df):
    return df.sort_values('date')


def filter_df(df):
    df = sort_by_trace_time(df)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df = delete_not_use_trace(df)
    df.drop_duplicates(
        subset=['date', 'trace_type', 'trace_obj', 'goods', 'income_and_expenses', 'amount', 'pay_way', 'status'],
        keep='first', inplace=True)

    # 拼接日期和金额并计算md5值
    df['id'] = df.apply(lambda x: hashlib.md5((str(x['date']) + x['amount']).encode()).hexdigest(), axis=1)

    # 对原始文件中标记的内容进行处理
    df_remark = load_remark_info()
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


def load_wechat_trace():
    df = pd.DataFrame()
    for f in os.listdir(trade_path):
        if '微信支付' not in f:
            continue
        inner_df = pd.DataFrame(fmt.format_wechat_to_list(trade_path + f))
        inner_df.columns = inner_df.iloc[0]
        inner_df = inner_df[1:]
        df = pd.concat([df, inner_df])
    df = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8]]
    df.columns = ['date', 'trace_type', 'trace_obj', 'goods', 'income_and_expenses', 'amount', 'pay_way', 'status', 'order_no']
    df['source'] = 'wechat'
    df = filter_df(df)
    df = format_amount(df)
    return df


def load_alipay_trace():
    df = pd.DataFrame()
    for f in os.listdir(trade_path):
        if 'alipay' not in f:
            continue
        inner_df = pd.DataFrame(fmt.format_alipay_to_list(trade_path + f))

        # 把第一行当做表头并删除第一行
        inner_df.columns = inner_df.iloc[0]
        inner_df = inner_df[1:]

        # 如果是新版格式的导出，删除最后一列备注
        if inner_df.columns[0].strip() == '交易时间':
            # 使用 .drop() 方法删除最后一列
            inner_df.drop(inner_df.columns[-1], axis=1, inplace=True)

        df = pd.concat([df, inner_df])
    if df.columns[0].strip() == '交易时间':
        df = df.iloc[:, [0, 1, 2, 4, 5, 6, 7, 8, 9]]
    if df.columns[0].strip() == '收/支':
        df = df.iloc[:, [10, 7, 1, 3, 0, 5, 4, 6, 8]]
    df.columns = ['date', 'trace_type', 'trace_obj', 'goods', 'income_and_expenses', 'amount', 'pay_way', 'status', 'order_no']
    df['source'] = 'alipay'
    df = filter_df(df)
    df = format_amount(df)
    return df


def load_all_trace():
    df = pd.concat([load_wechat_trace(), load_alipay_trace()])
    df = df.sort_values(by='date')
    return df


if __name__ == '__main__':
    all_df = load_all_trace()
    print(len(all_df))
    print(all_df.head())
