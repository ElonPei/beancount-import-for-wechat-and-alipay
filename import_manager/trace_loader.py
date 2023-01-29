import os

import pandas as pd

import import_manager.formater_csv as fmt

trade_path = '/Users/peiel/Desktop/123/'


def sort_by_trace_time(df):
    return df.sort_values('date')


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
    df.columns = ['date', 'trace_type', 'trace_obj', 'good', 'income_and_expenses', 'amount', 'pay_way', 'status']
    df['source'] = 'wechat'
    df = sort_by_trace_time(df)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
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
    df.columns = ['date', 'trace_type', 'trace_obj', 'good', 'income_and_expenses', 'amount', 'pay_way', 'status']
    df['source'] = 'alipay'
    df = sort_by_trace_time(df)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return df


if __name__ == '__main__':
    wechat_df = load_wechat_trace()
    print(wechat_df.head())
    alipay_df = load_alipay_trace()
    print(alipay_df.head())

