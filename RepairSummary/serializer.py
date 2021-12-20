from rest_framework import serializers
from .models import RepairSummary
from date.serializer import DateSerializer
from diagnosis.serializer import DiagnosisSerializer
from client.serializer import ClientSerializer
from status.serializer import StatusSerializer
from motorcycle.serializer import MotorcycleSerializer
# Create a model serializer 
class RepairSummarySerializer(serializers.ModelSerializer):
    date = DateSerializer(read_only=True)
    diagnosis = DiagnosisSerializer(read_only=True)
    client = ClientSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    motorcycle = MotorcycleSerializer(read_only=True)
    RepairSummary.objects.order_by('id')
    # specify model and fields
    class Meta:
        model = RepairSummary
        fields = '__all__'

class AddRepairSummarySerializer(serializers.ModelSerializer):

    # specify model and fields
    class Meta:
        model = RepairSummary
        fields = '__all__'