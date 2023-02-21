import pandas as pd


def find_pob_pay_way(row, df):
    order_no = row['order_no']
    order_no = order_no if '_' not in order_no else order_no.split('_')[0]
    source = row['source']
    find_df = pd.DataFrame()
    if 'alipay' == source:
        find_df = df.loc[df['business_order_no'] == order_no]
    if 'wechat' == source:
        find_df = df.loc[(df['order_no'] == order_no) & (df['goods'].str.contains('亲属卡'))]
    if find_df.empty:
        return row['pay_way']
    else:
        return find_df.iloc[0]['pay_way']


def payment_on_behalf(df):
    # 找到所有支付方代付的交易，把代付方的付款方式赋值到支付方上
    condition = (df['pay_way'].str.contains('亲情卡')) | (df['pay_way'].str.contains('亲属卡'))
    df.loc[condition, 'pay_way'] = df.loc[condition].apply(find_pob_pay_way, df=df, axis=1)
    # 删除代付方的交易记录
    condition_del = (df['goods'].str.contains('亲情卡')) | (df['goods'].str.contains('亲属卡'))
    list_index = list(df.loc[condition_del].index.values)
    df = df.drop(list_index, axis='index')
    return df
