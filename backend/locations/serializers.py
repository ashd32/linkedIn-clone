from rest_framework import serializers
from .models import City, Country


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = (
            'city_id',
            'name',
            'parent_id',
        )


class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)
    class Meta:
        model = Country
        fields = (
            'country_id',
            'name',
            'cities'
        )