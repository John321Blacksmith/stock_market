from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class CustomUserModelDataTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.user = get_user_model().objects.create_user(
					username='Test User',
					password='test123',
					email='test@mail.com',
			)

	def test_model_data(self):
		self.assertEqual(self.user.username, 'Test User')
		self.assertEqual(self.user.email, 'test@mail.com')