from django.shortcuts import render
from .models import Product, Category
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializer import CategorySerializer, ProductSerializer


# Here our only motive is to get list of all the Catagory.
class CategoryListViews(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# For Listing all products
class ProductListViews(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

# For Listing the perticular product
class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    lookup_field = 'pk'