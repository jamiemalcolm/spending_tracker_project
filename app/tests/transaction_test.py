import unittest

from app.models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction("Sainsbury's", "Groceries", 4.59)

    def test_transaction_has_merchant(self):
        self.assertEqual("Sainsbury's", self.transaction.merchant)

    def test_transaction_has_tag(self):
        self.assertEqual("Groceries", self.transaction.tag)

    def test_transaction_has_amount(self):
        self.assertEqual(4.59, self.transaction.amount)

    # def test_transaction_has_date(self):
    #     self.assertEqual(, self.transaction.amount)