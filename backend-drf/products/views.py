from django.shortcuts import render
from .models import Product, Category
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializer import CategorySerializer, ProductSerializer

# Create your views here.
class CategoryListViews(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListViews(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'