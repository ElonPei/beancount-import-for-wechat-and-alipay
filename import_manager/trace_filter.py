def filter_df(df):
    df = df.loc[df['status'] != '交易关闭']
    return df
