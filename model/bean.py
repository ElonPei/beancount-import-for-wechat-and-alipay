class Bean:
    def __init__(self, id, remark, date, trace_type, location, desc, items, income_and_expenses, pay_way, trace_obj,
                 log_org_trace, log_change_rule,
                 log_new_trace, ):
        self.id = id
        self.remark = remark
        self.date = date
        self.trace_type = trace_type
        self.location = location
        self.desc = desc
        self.income_and_expenses = income_and_expenses
        self.pay_way = pay_way
        self.trace_obj = trace_obj

        self.items = items

        self.log_org_trace = log_org_trace
        self.log_change_rule = log_change_rule
        self.log_new_trace = log_new_trace

    def __str__(self):
        items = ''
        for item in self.items:
            items = items + '\t[' + str(item) + ']\n'
        return 'date -> ' + self.date + ', location -> ' + self.location + ', desc -> ' + self.desc + ', items -> \n' + items


class Item:
    def __init__(self, account, amount=None, account_rule=None):
        self.account = account
        self.account_rule = account_rule
        self.amount = amount
        self.currency = 'CNY'

    def __str__(self):
        return 'account -> ' + self.account + ', amount -> ' + str(self.amount) + ', currency -> ' + self.currency
