from trace_processor.trace_account_conf import AccountConf


def account_match(df):
    income_conditions = df['income_and_expenses'] == '收入'
    expenses_conditions = df['income_and_expenses'] == '支出'

    # 目标账户的处理
    df['desc_account'] = ''
    df['desc_account_rule'] = ''
    ## 收入的情况
    income = AccountConf.income

    def income_match(row):
        trace_obj = row['trace_obj']
        remark = row['remark']
        if remark in income:
            return income[remark]
        for key in income:
            if key in trace_obj:
                return income[key]
        return income['未知']

    def income_match_rule(row):
        for key in income:
            if key in row['trace_obj']:
                return key + ' -> ' + income[key]
        return ''

    df.loc[income_conditions, 'desc_account'] = df.loc[income_conditions].apply(income_match, axis=1)
    df.loc[income_conditions, 'desc_account_rule'] = df.loc[income_conditions].apply(income_match_rule, axis=1)

    ## 支出的情况
    expenses = AccountConf.expenses

    def expense_match(row):
        remark = row['remark']
        trace_obj = row['trace_obj']
        goods = row['goods']

        if remark in expenses:
            return expenses[remark]
        for key in expenses:
            if key in remark or key in trace_obj or key in goods:
                return expenses[key]
        return expenses['未知']

    def expense_match_rule(row):
        remark = row['remark']
        if remark in expenses:
            return remark + ' -> ' + expenses[remark]
        for key in expenses:
            if key in remark or key in row['trace_obj'] or key in row['goods']:
                return key + ' -> ' + expenses[key]
        return ''

    df.loc[expenses_conditions, 'desc_account'] = df.loc[expenses_conditions].apply(expense_match, axis=1)
    df.loc[expenses_conditions, 'desc_account_rule'] = df.loc[expenses_conditions].apply(expense_match_rule, axis=1)

    # 当前账户的处理
    df['pre_account'] = ''

    def pay_way_match(row):
        assets = AccountConf.assets
        liabilities = AccountConf.liabilities

        pay_way = row['pay_way']
        # 兼容招行交易时的描述
        if '&' in pay_way:
            pay_way = pay_way.split('&')[0]
        if pay_way in assets:
            return assets[pay_way]
        if pay_way in liabilities:
            return liabilities[pay_way]
        return assets['未知']

    ## 收入的情况
    df.loc[income_conditions, 'pre_account'] = df.loc[income_conditions].apply(pay_way_match, axis=1)
    ## 支出的情况
    df.loc[expenses_conditions, 'pre_account'] = df.loc[expenses_conditions].apply(pay_way_match, axis=1)

    return df
