"""
转账处理
"""

allocation_of_funds_conf = {
    'trace_obj': "裴二龙|哈哈୧(๑•̀⌄•́๑)૭|发给Aimee",
}


def sign_allocation_of_funds(df):
    """
    标记资金调拨的数据
    """
    for k, v in allocation_of_funds_conf.items():
        for item in v.split('|'):
            df.loc[(df[k] == item) & (df['remark'] == ''), 'is_allocation_funds'] = '1'
    return df


def transfer(df):
    if df.empty:
        return df
    df = sign_allocation_of_funds(df)
    return df
