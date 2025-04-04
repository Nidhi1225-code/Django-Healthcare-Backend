from rest_framework import serializers
from .models import Scan
from .models import Patient

class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = ['patient', 'scan_image', 'result', 'uploaded_at']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields='__all__'