class Bean:
    def __init__(self, id, remark, tags, date, trace_type, trace_obj, desc, items, income_and_expenses, pay_way,
                 status, order_no, source, trace_change_rule):
        self.id = id
        self.remark = remark
        self.tags = tags
        self.date = date
        self.trace_type = trace_type
        self.trace_obj = trace_obj
        self.desc = desc
        self.income_and_expenses = income_and_expenses
        self.pay_way = pay_way
        self.status = status
        self.order_no = order_no
        self.source = source
        self.trace_change_rule = trace_change_rule


        self.items = items

    def __str__(self):
        items = ''
        for item in self.items:
            items = items + '\t[' + str(item) + ']\n'
        return 'date -> ' + self.date + ', trace_obj -> ' + self.trace_obj + ', desc -> ' + self.desc + ', items -> \n' + items


class Item:
    def __init__(self, account, amount=None, account_rule=None):
        self.account = account
        self.account_rule = account_rule
        self.amount = amount
        self.currency = 'CNY'

    def __str__(self):
        return 'account -> ' + self.account + ', amount -> ' + str(self.amount) + ', currency -> ' + self.currency
