from trace_convert.trace_account_conf import account_map
from trace_convert.trace_account_conf import trace_change_map


def match(account):
    for k, v in account_map['assets'].items():
        if account == k:
            return v
    for k, v in account_map['liabilities'].items():
        if account == k:
            return v
    return account


def convert_account(beans):
    for bean in beans:
        for item in bean.items:
            account = item.account
            item.account = match(account)
    return beans


def convert_trace_change(row):
    for rule, v in trace_change_map.items():
        if rule.split('=')[1] in row[rule.split('=')[0]]:
            row[v.split('=')[0]] = v.split('=')[1]
    return row
