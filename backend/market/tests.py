from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Purchase, Sale
from .options import EXCHANGES
# Create your tests here.


class OrderModelDataTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.user = get_user_model().objects.create_user(
					username='Test User',
					password='test123',
					email='test@mail.com',
			)


	def test_demo_object_exists(self):
		random_object = Purchase.return_random_object()

		status = random_object.status
		instrument = random_object.instrument

		self.assertEqual(random_object.status, status)
		self.assertIn(instrument[1], EXCHANGES)
		self.assertNotEqual(random_object.amount, 0)
		self.assertNotEqual(random_object.price, 0)


	def test_purchase_created_when_user_buys(self):
		request_data = {
			'amount': 99999.9999,
			'price': 9999.9999,
			'instrument': 'GBP/USD',
		}
		# when user hits BUY button, purchase object is formed
		purchase = self.user.buy(**request_data)
		# test if the order is a purchase
		# with corresponding data from the
		# request data
		self.assertEqual(purchase.status,'Active' )
		self.assertEqual(purchase.return_side(), 'purchase')
		self.assertEqual(purchase.amount, request_data['amount'])
		self.assertEqual(purchase.price, request_data['price'])
		self.assertIn(purchase.instrument, EXCHANGES)

		# test if the purchase belongs to the user
		self.assertEqual(purchase.user.username, 'Test User')

	def test_sale_created_when_user_sells(self):
		request_data = {
			'amount': 111111.11111,
			'price': 111111.11111,
			'instrument': 'USD/JPY',
		}
		# when user hits SELL button, sell object is formed
		sale = self.user.sell(**request_data)
		# test if the order is a sale
		# with corresponding data from the
		# request data
		self.assertEqual(sale.status, 'Active')
		self.assertEqual(sale.return_side(), 'sale')
		self.assertEqual(sale.amount, request_data['amount'])
		self.assertEqual(sale.price, request_data['price'])
		self.assertIn(sale.instrument, EXCHANGES)

		# test if the purchase belongs to the user
		self.assertEqual(sale.user.username, 'Test User')