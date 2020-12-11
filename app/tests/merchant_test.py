import unittest
from app.models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.merchant = Merchant("Sainsbury's")

    def test_merchant_has_name(self):
        self.assertEqual("Sainsbury's", self.merchant.name)

    def test_merchant_has_active(self):
        self.assertEqual(True, self.merchant.active)
