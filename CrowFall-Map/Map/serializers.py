from rest_framework import serializers
from Map.models import Map, Dot, Category


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        exclude = []


class DotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dot
        exclude = []


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []
