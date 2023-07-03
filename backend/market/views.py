from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Purchase, Sale
from .serializers import OrderSerializer, PurchaseSerializer, SaleSerializer

# Create your views here.


class TicketView(APIView):
	"""
	Main Ticket API endpoint.
	"""
	def get(self, request):
		"""
		See a main page with
		random data.
		"""
		random_object = Purchase.return_random_object()
		serializer = OrderSerializer(random_object)
		return Response(serializer.data)

	def post(self, request):
		"""
		Push either SELL or
		BUY button and create
		a new order so the server
		begins to search opposite
		ones.
		"""
		...


class RecentOrdersList(APIView):
	...


class ActiveOrdersList(APIView):
	def get(self, request, format=None):
		...


class ActiveOrderDetail(APIView):
	def get(self, request, pk, format=None):
		...


class PurchaseList(APIView):
	def get(self, request, format=None):
		...


class SalesList(APIView):
	def get(self, request, format=None):
		...

