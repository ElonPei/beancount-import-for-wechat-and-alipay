class Bean:
    def __init__(self, date, location, desc, items):
        self.date = date
        self.location = location
        self.desc = desc
        self.items = items

    def __str__(self):
        items = ''
        for item in self.items:
            items = items + '\t[' + str(item) + ']\n'
        return 'date -> ' + self.date + ', location -> ' + self.location + ', desc -> ' + self.desc + ', items -> \n' + items


class Item:
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.currency = 'CNY'

    def __str__(self):
        return 'account -> ' + self.account + ', amount -> ' + str(self.amount) + ', currency -> ' + self.currency
