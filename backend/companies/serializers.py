from rest_framework import serializers
from .models import Company, Office


class OfficeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Office
        fields = '__all__'
       

class CompanySerializer(serializers.ModelSerializer):
    offices = OfficeSerializer(many=True, required=True)
    class Meta:
        model = Company
        fields = '__all__'


