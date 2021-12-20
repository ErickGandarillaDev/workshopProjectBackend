from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializer import DateSerializer
from .models import Date
from rest_framework.permissions import IsAuthenticated

class DateViewSet(viewsets.ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer