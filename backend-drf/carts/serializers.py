from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name') #We also pass product name in recursive api
    price = serializers.DecimalField(source='product.price', max_digits=6, decimal_places=2)
    tax_percent = serializers.DecimalField(source='product.tax_percentage', max_digits=10, decimal_places=2)
    
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True) # This 'items=' is very important..... Belongs to models.py

    '''
    # Why we are explicitly mention to serializer..?
    # Because modelserializer gives serialized output which are present only in database, 
    # But we are using function/ property so we need to pass those method explicitly
    '''
    subtotal = serializers.DecimalField(max_digits=6, decimal_places=2)
    tax_amount = serializers.DecimalField(max_digits=6, decimal_places=2)
    grand_total = serializers.DecimalField(max_digits=6, decimal_places=2)

    # related_name='items' ==============> line no 17
    # It should be same name
    class Meta:
        model = Cart
        fields = '__all__'


