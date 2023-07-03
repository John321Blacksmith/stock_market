import random
from django.conf import settings
from django.db import models
from .options import EXCHANGES
# Create your models here.


INSTRUMENTS = [(str(index), EXCHANGES[index]) for index in range(1, len(EXCHANGES))]

class Order(models.Model):
	"""
	This model represents
	every order wether it
	is a purchase or sale.
	"""
	time_created = models.DateTimeField(auto_now_add=True)
	time_changed = models.DateTimeField(auto_now_add=True)
	status = models.CharField(default='Active', max_length=25)
	price = models.DecimalField(max_digits=14, decimal_places=5, null=True)
	amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)
	instrument = models.CharField(choices=INSTRUMENTS, max_length=9)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

	class Meta:
		abstract = True

	def return_side(self):
		"""
		This method returns a
		one of two options the
		user does.
		"""
		return self.side

	@classmethod
	def return_random_object(cls):
		cls.random_object = cls(
				price=random.randint(1, 9999999999) / 100000,
				amount=random.randint(1, 99999999) / 100,
				instrument=random.choice(INSTRUMENTS),
			)

		return cls.random_object


class Purchase(Order):
	"""
	This model represents
	every purchase.
	"""
	side = 'purchase'

class Sale(Order):
	"""
	This model represents
	every sale.
	"""
	side = 'sale'