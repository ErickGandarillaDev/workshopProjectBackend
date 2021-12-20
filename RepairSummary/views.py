from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

# import local data
from .serializer import RepairSummarySerializer
from .serializer import AddRepairSummarySerializer
from .models import RepairSummary




class RepairSummaryViewSet(ModelViewSet):

    queryset = RepairSummary.objects.all().order_by('id')
    serializer_class = RepairSummarySerializer


class AddRepairSummaryViewSet(ModelViewSet):

    queryset = RepairSummary.objects.all().order_by('id')
    serializer_class = AddRepairSummarySerializer