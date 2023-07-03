from django.urls import path
from . import views


urlpatterns = [
	path('', views.TicketView.as_view()),
	path('recent-orders/', views.RecentOrdersList.as_view()),
	path('active-orders/', views.ActiveOrdersList.as_view()),
	path('active-orders/<int:pk>/', views.ActiveOrderDetail.as_view()),
	path('purchases/', views.PurchaseList.as_view()),
	path('sales/', views.SalesList.as_view()),
] 