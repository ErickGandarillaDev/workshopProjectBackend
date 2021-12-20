from rest_framework import serializers
from .models import Diagnosis
 


class DiagnosisSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Diagnosis
        fields = '__all__'

