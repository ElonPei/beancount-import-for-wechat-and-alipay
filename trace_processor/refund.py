import hashlib
import re

import pandas as pd


def get_amount_by_str(s):
    # 匹配金额数值的正则表达式
    pattern = r'\d+\.\d+'
    # 提取金额数值
    match = re.search(pattern, s)
    if match:
        amount = float(match.group())
        return amount
    raise Exception('无法提取字符串中数据', s)


def wechat_refund(df):
    """
    微信支付退款数据的处理
    """
    # 筛选出所有微信支付的退款数据
    conditions = (df['source'] == 'wechat') & \
                 ((df['status'].str.contains('已退款')) | (df['status'] == '已全额退款'))
    refund_df = df.loc[conditions]
    # 对退款数据中收支类型为收入的数据做删除处理
    df_delete_conditions = conditions & (df['income_and_expenses'] == '收入')
    df = df.loc[~df_delete_conditions]
    # 对退款数据中收支类型为支出的数据做负支出抵消处理
    refund_df = refund_df.loc[refund_df['income_and_expenses'] == '支出']
    for index, row in refund_df.iterrows():
        new_row = row.copy()
        if new_row['status'] == '已全额退款':
            new_row['amount'] = new_row['amount'] * -1
        elif new_row['status'].startswith('已退款'):
            new_row['amount'] = get_amount_by_str(new_row['status']) * -1
        # 拼接日期和金额并计算md5值
        new_row['id'] = hashlib.md5((str(new_row['date']) + str(new_row['amount'])).encode()).hexdigest()
        df = pd.concat([df, new_row.to_frame().T], ignore_index=True)
    return df


def alipay_refund(df):
    """
    微信支付退款数据的处理
    """
    # 筛选出来所有退款流水, 把退款的数据直接替换为负支出即可
    conditions = (df['source'] == 'alipay') & \
                 (df['status'] == '退款成功')
    df.loc[conditions, 'income_and_expenses'] = '支出'
    df.loc[conditions, 'amount'] = df.loc[conditions, 'amount'] * -1
    return df


def refund(df):
    if df.empty:
        return df

    df = wechat_refund(df)
    df = alipay_refund(df)
    return df
