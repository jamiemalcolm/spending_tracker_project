class Transaction:

    def __init__(self, merchant, tag, amount, id = None, time_stamp = None):
        self.merchant = merchant
        self.tag = tag
        self.amount = amount
        self.id = id
        self.time_stamp = time_stamp