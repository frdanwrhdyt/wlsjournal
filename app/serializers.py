from .models import *
from rest_framework import serializers

class UserBusinessSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserBusiness
        fields = '__all__'
    
class PurchaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseProduct
        fields = '__all__'

class SellingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellingProduct
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
            