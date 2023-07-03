import json
from channels.db import database_sync_to_async




class StockConsumer:
	"""
	This class creates a consumer 
	object per each new user and 
	facilitates all available 
	event handlers that take
	place in the channel layer.
	"""
	
	async def connect(self):
		"""
		When a new user connects
		to the stock server, he
		is checked for auth.
		"""
		await self.accept()

	async def disconnect(self):
		await self.disconnect()

	async def serve(self):
		...