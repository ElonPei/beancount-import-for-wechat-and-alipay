class Bean:
    def __init__(self, date, location, desc, items, income_and_expenses, org_trace, change_rule, new_trace):
        self.date = date
        self.location = location
        self.desc = desc
        self.items = items
        self.income_and_expenses = income_and_expenses
        self.org_trace = org_trace
        self.change_rule = change_rule
        self.new_trace = new_trace


    def __str__(self):
        items = ''
        for item in self.items:
            items = items + '\t[' + str(item) + ']\n'
        return 'date -> ' + self.date + ', location -> ' + self.location + ', desc -> ' + self.desc + ', items -> \n' + items


class Item:
    def __init__(self, account, amount, account_rule=None):
        self.account = account
        self.account_rule = account_rule
        self.amount = amount
        self.currency = 'CNY'

    def __str__(self):
        return 'account -> ' + self.account + ', amount -> ' + str(self.amount) + ', currency -> ' + self.currency
