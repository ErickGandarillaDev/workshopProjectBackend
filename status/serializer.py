from rest_framework import serializers
from .models import Status
 


class StatusSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Status
        fields = '__all__'