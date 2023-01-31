from model.bean import Item
from trace_convert.trace_account_conf import account_map
from trace_convert.trace_account_conf import trace_change_map


def match(account):
    for k, v in account_map['assets'].items():
        for i in k.split('|'):
            if account == i:
                return v, k + '->' + v
    for k, v in account_map['liabilities'].items():
        for i in k.split('|'):
            if account == i:
                return v, k + '->' + v
    return account, 'NotFoundRule'


def match_expenses(bean):
    for k, v in account_map['expenses'].items():
        for i in k.split('|'):
            if i in bean.desc or i in bean.location:
                return v, k + '->' + v
    return 'Expenses:Unknown', 'NotFoundExpensesRule'


def match_income(bean):
    for k, v in account_map['income'].items():
        for i in k.split('|'):
            if i in bean.desc or i in bean.location:
                return v, k + '->' + v
    return 'Income:Unknown', 'NotFoundIncomeRule'


def convert_account(beans):
    for bean in beans:
        item = bean.items[0]

        # 相关账户
        account, rule = match(item.account)
        related_account_item = Item(account=account, amount=None, account_rule=rule)
        bean.items.append(related_account_item)

        # 支出的情况
        if item.amount >= 0:
            account, rule = match_expenses(bean)
            item.account = account
            item.account_rule = rule
        # 收入的情况
        if item.amount < 0:
            account, rule = match_income(bean)
            item.account = account
            item.account_rule = rule

    return beans


def convert_trace_change(row):
    for rule, v in trace_change_map.items():
        if rule.split('=')[1] in row[rule.split('=')[0]]:
            row[v.split('=')[0]] = v.split('=')[1]
    return row
