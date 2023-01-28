import os

import pandas as pd

import import_manager.formater_csv as fmt

trade_path = '/Users/peiel/Desktop/123/'


def sort_by_trace_time(df):
    return df.sort_values('交易时间')


def load_wechat_trace():
    df = pd.DataFrame()
    for f in os.listdir(trade_path):
        if '微信支付' not in f:
            continue
        inner_df = pd.DataFrame(fmt.format_wechat_to_list(trade_path + f))
        inner_df.columns = inner_df.iloc[0]
        inner_df = inner_df[1:]
        df = pd.concat([df, inner_df])
    df = sort_by_trace_time(df)
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
    df.columns = ['收/支','交易对方','对方账号','商品说明','收/付款方式','金额','交易状态','交易分类','交易订单号','商家订单号','交易时间', '']
    df = sort_by_trace_time(df)
    return df


if __name__ == '__main__':
    wechat_df = load_wechat_trace()
    print(wechat_df.head())
    alipay_df = load_alipay_trace()
    print(alipay_df.head())

