from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializer import StatusSerializer
from .models import Status
from rest_framework.permissions import IsAuthenticated

class StatusViewSet(viewsets.ModelViewSet):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer