import os

import pandas as pd

import import_manager.formater_csv as fmt

trade_path = '/Users/peiel/Desktop/123/'


def sort_by_trace_time(df):
    return df.sort_values('交易时间')


def load_wechat_trace():
    df = pd.DataFrame()
    for f in os.listdir(trade_path):
        inner_df = pd.DataFrame(fmt.format_wechat_to_list(trade_path + f))
        inner_df.columns = inner_df.iloc[0]
        inner_df = inner_df[1:]
        df = pd.concat([df, inner_df])
    df = sort_by_trace_time(df)
    return df


def load_alipay_trace():
    df = pd.DataFrame()
    for f in os.listdir(trade_path):
        inner_df = pd.DataFrame(fmt.format_alipay_to_list(trade_path + f))
        inner_df.columns = inner_df.iloc[0]
        inner_df = inner_df[1:]
        df = pd.concat([df, inner_df])
    df = sort_by_trace_time(df)
    return df


if __name__ == '__main__':
    wechat_df = load_wechat_trace()
    print(wechat_df)
