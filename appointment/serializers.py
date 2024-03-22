# serializers.py
from rest_framework import serializers
from .models import AppointmentTable

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentTable
        fields = '__all__'