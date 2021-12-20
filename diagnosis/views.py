from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializer import DiagnosisSerializer
from .models import Diagnosis
from rest_framework.permissions import IsAuthenticated

class DiagnosisViewSet(viewsets.ModelViewSet):

    queryset = Diagnosis.objects.all().order_by('id')
    serializer_class = DiagnosisSerializer