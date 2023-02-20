import os
import re

from import_manager.trace_loader import load_all_trace
from trace_processor.trace_change import trace_change


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
    wechat_refund_df = df.loc[conditions]
    # 对退款数据中收支类型为收入的数据做删除处理
    df_delete_conditions = conditions & (df['income_and_expenses'] == '收入')
    df = df.loc[~df_delete_conditions]
    # 对退款数据中收支类型为支出的数据做负支出抵消处理
    wechat_refund_df = wechat_refund_df.loc[wechat_refund_df['income_and_expenses'] == '支出']
    for index, row in wechat_refund_df.iterrows():
        new_row = row.copy()
        if new_row['status'] == '已全额退款':
            new_row['amount'] = new_row['amount'] * -1
        elif new_row['status'].startswith('已退款'):
            new_row['amount'] = get_amount_by_str(new_row['status']) * -1
        df.loc[len(df.index)] = new_row
    return df


def alipay_refund(df):
    return df


def refund(df):
    df = wechat_refund(df)
    df = alipay_refund(df)
    return df


if __name__ == '__main__':
    all_df = load_all_trace()
    print(len(all_df))
    all_df = trace_change(all_df)
    all_df = refund(all_df)
    print(all_df.head())
    print(all_df.columns)
    all_df.to_csv('example.csv', index=False)
    os.system('open example.csv')
