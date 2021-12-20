from rest_framework import serializers
from .models import Client
 


class ClientSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Client
        fields = '__all__'

