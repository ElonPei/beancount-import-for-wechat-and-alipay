from model.bean import Item
from trace_convert.trace_account_conf import account_map
from trace_convert.trace_account_conf import trace_change_map


def match(account):
    for k, v in account_map['assets'].items():
        for i in k.split('|'):
            if account == i:
                return v
    for k, v in account_map['liabilities'].items():
        for i in k.split('|'):
            if account == i:
                return v
    return account


def match_expenses(bean):
    for k, v in account_map['expenses'].items():
        for i in k.split('|'):
            if i in bean.desc or i in bean.location:
                return v
    return 'Expenses:Unknown'


def match_income(bean):
    for k, v in account_map['income'].items():
        for i in k.split('|'):
            if i in bean.desc or i in bean.location:
                return v
    return 'Income:Unknown'


def convert_account(beans):
    for bean in beans:
        item = bean.items[0]

        # 相关账户
        related_account_item = Item(account=match(item.account), amount=None)
        bean.items.append(related_account_item)

        # 支出的情况
        if item.amount >= 0:
            item.account = match_expenses(bean)
        # 收入的情况
        if item.amount < 0:
            item.account = match_income(bean)

    return beans


def convert_trace_change(row):
    for rule, v in trace_change_map.items():
        if rule.split('=')[1] in row[rule.split('=')[0]]:
            row[v.split('=')[0]] = v.split('=')[1]
    return row
