from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Map.models import Map, Dot, Category
from Map.serializers import MapSerializer, DotSerializer, CategorySerializer
from rest_framework import routers, viewsets


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    lookup_fields = ["location_name", "type_of_location"]


class DotViewSet(viewsets.ModelViewSet):
    queryset = Dot.objects.all()
    serializer_class = DotSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
