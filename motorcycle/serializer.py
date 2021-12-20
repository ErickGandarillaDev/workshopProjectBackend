from rest_framework import serializers
from .models import Motorcycle
 


class MotorcycleSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Motorcycle
        fields = '__all__'

