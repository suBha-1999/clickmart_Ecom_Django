from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from carts.models import Cart, CartItem
from .utils import send_order_notification


# Create your views here.
class PlaceOrderViews(APIView):
    # Check if user is logged in
    permission_classes = [IsAuthenticated]

    # Check If the cart is empty, if yes return empty Cart
    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        shipping_address = request.data.get('shippingAddress')
        # print(shipping_address)

        #  If cart is not empty, create Order
        if not cart or cart.items.count() == 0:
            return Response({'error': 'Cart is empty'})

        order = Order.objects.create(
            user = request.user,
            subtotal = cart.subtotal,
            tax_amount = cart.tax_amount,
            grand_total = cart.grand_total,
            status = 'CONFIRMED',
            address = shipping_address.get('address'),
            phone = shipping_address.get('phone'),
            city = shipping_address.get('city'),
            state = shipping_address.get('state'),
            zipCode = shipping_address.get('zipCode'),
        )
        # print(order)
        for item in cart.items.all():
            product = item.product

            # check quantity
            if product.stock < item.quantity:
                return Response({"details" : f"Only {product.stock} is left for {product.name}"},
                                status=status.HTTP_400_BAD_REQUEST)
            
            # decrese the quantity
            product.stock -= item.quantity
            product.save()

        # Create the Order items and save the data
        for item in cart.items.all():
            OrderItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price, 
                total_price = item.total_price             
            )

        # Clear the cart
        cart.items.all().delete()
        cart.save()

        '''
        # Send a notification Email

        as we have DATABASE_Connection, same we have SMTP_Connection for this
        '''
        send_order_notification(order)


        # Send a notification to FrontEnd
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class myOrdersView(ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer
    # queryset = Order.objects.all() #This will give all user's order, that we don't want
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    


class OrderDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        order = get_object_or_404(Order, pk=pk, user=self.request.user)
        return order