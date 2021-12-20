from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializer import ClientSerializer
from .models import Client
from rest_framework.permissions import IsAuthenticated

class ClientViewSet(viewsets.ModelViewSet):
    """permission_classes=[IsAuthenticated]"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer