import unittest

from app.models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction("Sainsbury's", "Groceries", 4.59)

    def test_transaction_has_merchant(self):
        self.assertEqual("Sainsbury's", self.transaction.merchant)