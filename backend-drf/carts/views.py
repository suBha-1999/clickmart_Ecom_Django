from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer 
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CartListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        # if created:
        #     print('cart created')
        serializer = CartSerializer(cart)
        return Response(serializer.data)


        