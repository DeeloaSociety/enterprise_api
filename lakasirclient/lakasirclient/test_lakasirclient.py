from unittest import TestCase

from lakasir import LakasirClient

config = dict(
    base_url="http://127.0.0.1:8000",
    email="iyann1435@gmail.com",
    password="sriwijaya2"
)


class TestLakasirClient(TestCase):
    def setUp(self):
        self.lakasir = LakasirClient(**config)

    def test_authenticate(self):
        auth = self.lakasir.authenticate(config.get("email"), config.get("password"))
        self.assertIn('token', auth['data'])

    def test_me(self):
        me = self.lakasir.me()
        self.assertIsNotNone(me)

    def test_about(self):
        about = self.lakasir.about()
        self.assertIsNotNone(about)

    def test_transaction_sells(self):
        transaction = self.lakasir.transaction_sells()
        self.assertIsNotNone(transaction)

    def test_transaction_with_page(self):
        transaction = self.lakasir.transaction_sells()
        self.assertIn('current_page', transaction['data']['meta'])
        self.assertIn('per_page', transaction['data']['meta'])

    def test_total_sales(self):
        total_sales = self.lakasir.total_sales('today')
        self.assertIsNotNone(total_sales)

    def test_total_revenue(self):
        total_revenue = self.lakasir.total_revenue('today')
        self.assertIsNotNone(total_revenue)

    def test_total_gross_profit(self):
        total_gross_profit = self.lakasir.total_gross_profit('today')
        self.assertIsNotNone(total_gross_profit)
