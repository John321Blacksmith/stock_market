from django.urls import re_path
from . import consumers

# when the user pushes either buttons on the ticker page,
# he connects to the stock via websocket protocol

regex = '^ws/(?P<ticker_name>\w+)/$'

websocket_urlpatterns = [
	path('ws/stock/', consumers.StockConsumer()),
]