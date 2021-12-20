from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializer import MotorcycleSerializer
from .models import Motorcycle
from rest_framework.permissions import IsAuthenticated

class MotorcycleViewSet(viewsets.ModelViewSet):

    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer