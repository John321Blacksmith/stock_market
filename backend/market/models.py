import random
from django.db import models
from django.contrib.auth.models import User
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
	price = models.DecimalField(max_digits=14, decimal_places=5)
	amount = models.DecimalField(max_digits=11, decimal_places=2)
	instrument = models.CharField(choices=INSTRUMENTS, max_length=9)

	class Meta:
		abstract = True

	def return_side(self):
		"""
		This method returns a
		one of two options the
		user does.
		"""
		return self.__class__


class Purchase(Order):
	"""
	This model represents
	every purchase.
	"""

class Sale(Order):
	"""
	This model represents
	every sal.
	"""