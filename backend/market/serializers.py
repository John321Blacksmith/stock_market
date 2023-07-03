from rest_framework import serializers
from users.models import CustomUser
from market.models import Purchase, Sale, INSTRUMENTS


class OrderSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	time_created = serializers.DateTimeField(read_only=True)
	time_changed = serializers.DateTimeField(read_only=True)
	status = serializers.CharField(default='Active', max_length=25)
	price =  serializers.DecimalField(max_digits=14, decimal_places=5)
	amount = serializers.DecimalField(max_digits=11, decimal_places=2)
	instrument = serializers.ChoiceField(choices=INSTRUMENTS)
	user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
	side = serializers.CharField(max_length=10)


	def save(self, validated_data):
		return self.objects.create(**validated_data)


class PurchaseSerializer(OrderSerializer):
	class Meta:
		model = Purchase


class SaleSerializer(OrderSerializer):
	class Meta:
		model = Sale
