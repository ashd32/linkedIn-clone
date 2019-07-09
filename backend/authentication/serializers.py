from django.db import IntegrityError, transaction
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

from djoser import constants
from djoser.conf import settings
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from locations.serializers import CitySerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    photo = serializers.SerializerMethodField()
    city = CitySerializer()
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'full_name',
            'photo',
            'birthday',
            'city',
            'educations'
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def get_photo(self, obj):
        url = obj.photo.url if obj.photo else static(settings.BLANK_PHOTO)
        request = self.context.get("request", None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class UserCreateSerializer(UserCreateSerializer):
   pass