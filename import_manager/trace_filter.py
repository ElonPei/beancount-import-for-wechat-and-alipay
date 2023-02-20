def delete_not_use_trace(df):
    # df = df.loc[df['status'] != '交易关闭']
    # df = df.loc[df['status'] != '冻结成功']
    # df = df.loc[df['status'] != '代付关闭']
    # df = df.loc[df['status'] != '已关闭']
    # df = df.loc[df['status'] != '还款失败']
    # df = df.loc[df['status'] != '转账失败']
    # df = df.loc[df['status'] != '对方已退还']
    # df = df.loc[df['amount'] != '0.00']
    # df = df.loc[df['goods'] != '蚂蚁财富-天弘创业板ETF联接C[转换至]华宝中证银行ETF联接C']
    # df = df.loc[~df['goods'].str.contains('预授权解冻')]
    return df
