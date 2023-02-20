
def amount(df):
    # 收入为负数
    income_conditions = (df['income_and_expenses'] == '收入')
    df.loc[income_conditions, 'amount'] = abs(df.loc[income_conditions, 'amount']) * -1

    # 支出为正数
    expenses_conditions = (df['income_and_expenses'] == '支出')
    df.loc[expenses_conditions, 'amount'] = abs(df.loc[expenses_conditions, 'amount'])

    return df