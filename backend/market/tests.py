from django.test import TestCase
from .models import Purchase, Sale
from .options import EXCHANGES
# Create your tests here.


class OrderModelDataTest(TestCase):

	def test_demo_object_exists(self):
		random_object = Purchase.return_random_object()

		status = random_object.status
		instrument = random_object.instrument

		self.assertEqual(random_object.status, status)
		self.assertIn(instrument[1], EXCHANGES)
		self.assertNotEqual(random_object.amount, 0)
		self.assertNotEqual(random_object.price, 0)

	def test_purchase_model_data(self):
		purchase = Purchase.objects.create(instrument='EUR/USD', amount=457.853, price=332.890)
		self.assertEqual(purchase.status, 'Active')
		self.assertEqual(purchase.instrument, 'EUR/USD')
		self.assertEqual(purchase.amount, 457.853)
		self.assertEqual(purchase.price, 332.890)

	def test_sale_model_data(self):
		sale = Sale.objects.create(instrument='USD/EUR', amount=457.853, price=332.890)
		self.assertEqual(sale.status, 'Active')
		self.assertEqual(sale.instrument, 'USD/EUR')
		self.assertEqual(sale.amount, 457.853)
		self.assertEqual(sale.price, 332.890)