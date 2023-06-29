from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CustomUser(User):
	"""
	The traditional User model
	has been extended so
	every User has either 
	buy(), or sell() method.
	"""


	# the behavioral methods 
	# below take the data from
	# the JSON serializers
	def buy(self, *args, **kwargs):
		"""
		Perform a buying action.
		:returns: <Purchase obj>.
		"""
		return 

	def sell(self, *args, **kwargs):
		"""
		Perform a selling
		action.
		:returns: <Sale obj>
		"""
		return 
