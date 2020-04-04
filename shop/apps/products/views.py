from rest_framework import generics
from .models import *
from .serializers import *


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductItemListView(generics.ListAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer


class ProductItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer


class ProductImageView(generics.RetrieveAPIView):
    queryset = ProductItemImage.objects.all()
    serializer_class = ProductImageSerializer