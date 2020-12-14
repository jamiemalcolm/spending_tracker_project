class Transaction:

    def __init__(self, merchant, tag, amount, id = None):
        self.merchant = merchant
        self.tag = tag
        self.amount = amount
        self.id = id

    
    
    # def convert_to_pennies(self, amount):
    #     before = int(amount * 100)
    #     return before        