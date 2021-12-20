from rest_framework import serializers
from .models import Date
 


class DateSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Date
        fields = '__all__'

