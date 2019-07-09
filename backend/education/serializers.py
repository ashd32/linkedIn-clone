from .models import UserEducation, Place
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            '__all__',
        )

class UserEducationSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    class Meta:
        model = UserEducation
        fields = (
            '__all__',
        )