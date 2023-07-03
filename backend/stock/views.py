from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse

from market.serializers import SaleSerializer, PurchaseSerializer

from market.models import Purchase, Sale

# Create your views here.


# def search_deal(order, matched_order=None):
# 	if order:
# 		if order.return_side() == 'purchase':
# 			matched_order = Sale.objects.get(pk=1)
# 		elif order.return_side() == 'sale':
# 			matched_order = Purchase.objects.get(pk=1)

# 		if matched_order:
# 			order.status = 'Filled'
# 			order.save()
# 			matched_order.delete()
# 		else:
# 			order.status = 'Rejected'

# 	return matched_order


# def perform_order(data, option: str, order=None) -> dict:
# 	user = get_user_model()
# 	if user.is_authenticated:
# 		if option.lower() == 'buy':
# 			order = user.buy(data)
# 		elif option.lower() == 'sell':
# 			order = user.sell(data)
# 	else:
# 		return reverse_lazy('auth')

# 	matched_order = search_deal(order)
# 	return matched_order


def index(request):
	"""
	Get a main ticker page with
	a random stock exchange sample
	and two buttons BUY and SELL.
	"""
	random_object = Purchase.return_random_object()
	return render(request, 'stock/ticker.html', context={'random_object': random_object})


def get_stock(request, button_choice):
	"""
	Get a place where there are
	many active orders of a
	corresponding side.
	"""
	order = perform_order(data=request.body, option=button_choice)
	return render(request, 'stock/saved_orders.html', {'order': order})


def get_active_orders(request):
	return render(request, 'stock/active_orders.html', context)


def get_saved_orders(request):
	return render(request, 'stock/saved_orders.html', context)