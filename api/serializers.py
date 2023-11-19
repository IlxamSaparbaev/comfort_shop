from rest_framework import serializers
from pages.models import (
    Product,
    Transport,
    Furniture,
    Cloth,
    Sport
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'

class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = '__all__'

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'