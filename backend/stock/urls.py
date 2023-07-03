from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='ticker'),
	path('stocks-table/<str:button_choice>/', views.get_stock, name='stocks_table'),
]