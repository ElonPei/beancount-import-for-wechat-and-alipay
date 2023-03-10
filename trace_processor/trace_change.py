from conf_manager.account_conf import AccountConf
from conf_manager.trace_change_conf import TraceChangeConf


def match_condition(df, rule_list):

    def match_rules(row, rules):
        for rule in rules:
            col, kw = rule.split('=')
            if row[col.strip()].find(kw.strip()) == -1:
                return False
        return True

    return df.apply(lambda row: match_rules(row, rule_list), axis=1)


def trace_change(df):
    if df.empty:
        return df
    conf = TraceChangeConf.trace_change
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

