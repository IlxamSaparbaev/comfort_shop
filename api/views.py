from rest_framework import generics
from pages.models import (
    Product,
    Transport,
    Furniture,
    Cloth,
    Sport
)
from .serializers import (
    ProductSerializer,
    TransportSerializer,
    FurnitureSerializer,
    ClothSerializer,
    SportSerializer
)

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPost(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPut(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDelete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
 