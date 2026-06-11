from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer,CartItemSerializer 
from rest_framework.response import Response
from rest_framework import status
from products.models import Product 

# Create your views here.
class CartListView(APIView):
    permission_classes = [IsAuthenticated] # need to login first to see cart 

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user) # True/ False
        # if created:
        #     print('cart created')
        serializer = CartSerializer(cart)
        # print(serializer.data)
        return Response(serializer.data)

# ================ For Add to Cart =======================
class AddToCart(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id') # frontend developer desing acording this, you have to tell him/her this value i need 
        quantity = request.data.get('quantity') # frontend developer desing acording this 

        if not product_id:
            return Response({'error': 'product_id is require'})
        
        # Add Product to the cart
        # First check for which product i want to add
        product = get_object_or_404(Product, id=product_id, is_active=True)

        # Then check if there any cart available for the user or not, if not just create
        cart, _ = Cart.objects.get_or_create(user=request.user) # if you dont want to use created you can put _
        # Here using created you can send me notification to user,
        # If there is no need of "created" you can use _

        # Also want to check that perticular product allready added in cart or not
        item, created = CartItem.objects.get_or_create(cart=cart, product=product) #quantity=1 by default
        
        # If created increse the quantity
        if not created:
            item.quantity += int(quantity)
            item.save()

        # After all that serialize your cart
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# ----------- For Stock Check and update ----------------------
class ManageCartItemView(APIView):
    permission_classes = [IsAuthenticated] # Only enter this section while you logged in.

    def patch(self, request, item_id): # we only need to update the quantity
        # print(request.data)
        # know about 'delta' 
        if 'change' not in request.data: # change value contain +1 or -1 for incress/decrese quantity
            return Response({"error": "change value is required"})
        
        change = int(request.data.get('change')) # Here we get the change value 
        # print(change)
        # Now we need to get that which item i want to change and who's cart is this....
        item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user) 
        # If we want to add items in CartItem, need to check user and item id,
        # But CartItem does not contain user, but Cart contain,
        # As CartItem linked with Cart using ForeignKey, we can access User by (cart__user).
        

        # Then we have to chect the stock of that product is availble or not
        product = item.product # item=CartItem -> Product

        if change > 0:
            if item.quantity + change > product.stock:
                return Response({'error': 'Not enough stock'})
            
        new_qty = item.quantity + change  #(2+1), (2 + -1)  

        if new_qty <= 0:
            item.delete()
            return Response({'sucess': 'item removed'})
        
        item.quantity = new_qty 
        item.save()
        serializer = CartItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def delete(self, request, item_id):
        item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)