def filter_df(df):
    df = df.loc[df['status'] != '交易关闭']
    df = df.loc[df['status'] != '冻结成功']
    return df
