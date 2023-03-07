import pandas as pd
"""
转账处理
"""

allocation_of_funds_conf = {
    'trace_obj': "裴二龙|哈哈୧(๑•̀⌄•́๑)૭|发给Aimee|卢娇艳(卢娇艳)",
}


def sign_allocation_of_funds(df):
    """
    标记资金调拨的数据
    """
    for k, v in allocation_of_funds_conf.items():
        for item in v.split('|'):
            df.loc[
                (df[k] == item) &
                (df['remark'] == '')
                , 'is_allocation_funds'] = '1'
    return df


def relation_fill(df):
    """
    填充 relation 字段，让其保证双向都有索引
    """
    current_relation_df = df.loc[df['relation'] != '']
    df_merge = pd.merge(df, current_relation_df, left_on='id', right_on='relation', how='left')
    df_merge.loc[df_merge['relation_x'] == '', 'relation_x'] = df_merge['id_y']
    df_merge = df_merge.iloc[:, :len(df.columns)]
    df_merge.columns = df.columns
    df_merge['relation'] = df_merge['relation'].fillna('')
    return df_merge


def process_fund_flow(df):
    """
    资金流转的情况的处理
    1. 通过 relation 字段查询关联id
    2. 如果收入金额大于等于支出的情况，保持收入不变的情况下，把支出交易修正为**正收入**（避免收支虚高）
    3. 如果收入金额小于支出的情况，保持支出不变的情况下，把收入交易修正为**负支出**（避免收支虚高）
    """
    df = relation_fill(df)
    relation_df = df.loc[df['relation'] != '']

    for index, row in relation_df.iterrows():
        if row['income_and_expenses'] == '支出':
            continue
        expenses_df = relation_df.loc[relation_df['id'] == row['relation']]
        if abs(row['amount']) >= abs(expenses_df['amount'].iloc[0]):
            # 步骤2
            df.loc[df['id'] == expenses_df['id'].iloc[0], 'income_and_expenses'] = '收入'
            df.loc[df['id'] == expenses_df['id'].iloc[0], 'amount'] = abs(expenses_df['amount'].iloc[0])
        else:
            # 步骤3
            df.loc[df['id']==row['id'], 'income_and_expenses'] = '支出'
            df.loc[df['id']==row['id'], 'amount'] = abs(row['amount']) * -1

    return df


def transfer(df):
    if df.empty:
        return df
    df = sign_allocation_of_funds(df)
    df = process_fund_flow(df)
    return df
