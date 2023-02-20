from import_manager.trace_loader import load_all_trace
from trace_processor.trace_account_conf import AccountConf


def match_condition(df, rule_list):

    def match_rules(row, rules):
        for rule in rules:
            col, kw = rule.split('=')
            if row[col.strip()].find(kw.strip()) == -1:
                return False
        return True

    return df.apply(lambda row: match_rules(row, rule_list), axis=1)


def trace_change(df):
    conf = AccountConf.trace_change
    for rules, values in conf.items():
        rule_list = [s.strip() for s in rules.split('&')]
        value_list = [s.strip() for s in values.split(',')]
        # 匹配所有符合条件的列
        conditions = match_condition(df, rule_list)
        # 对符合条件的列进行更新操作
        for value in value_list:
            k = value.split('=')[0].strip()
            v = value.split('=')[1].strip()
            df.loc[conditions, k] = v
            df.loc[conditions, 'trace_change_rule'] = rules + '->' + values
    return df


if __name__ == '__main__':
    all_df = load_all_trace()
    print(len(all_df))
    all_df = trace_change(all_df)
    print(all_df.head())
    print(all_df.columns)
    all_df.to_csv('example.csv', index=False)
