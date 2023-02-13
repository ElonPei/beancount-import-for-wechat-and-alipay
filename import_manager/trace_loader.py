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
    df = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7]]
    df.columns = ['date', 'trace_type', 'trace_obj', 'goods', 'income_and_expenses', 'amount', 'pay_way', 'status']
    df['source'] = 'wechat'
    df = filter_df(df)
    return df


def load_alipay_trace():
    df = pd.DataFrame()
    for f in os.listdir(trade_path):
        if 'alipay' not in f:
            continue
        inner_df = pd.DataFrame(fmt.format_alipay_to_list(trade_path + f))
        inner_df.columns = inner_df.iloc[0]
        inner_df = inner_df[1:]
        df = pd.concat([df, inner_df])
    df = df.iloc[:, [10, 7, 1, 3, 0, 5, 4, 6]]
    df.columns = ['date', 'trace_type', 'trace_obj', 'goods', 'income_and_expenses', 'amount', 'pay_way', 'status']
    df['source'] = 'alipay'
    df = filter_df(df)
    return df


if __name__ == '__main__':
    wechat_df = load_wechat_trace()
    print(wechat_df.head())
    alipay_df = load_alipay_trace()
    print(alipay_df.head())
