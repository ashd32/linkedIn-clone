from rest_framework import viewsets, permissions
from .models import City, Country
from .serializers import CountrySerializer, CitySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().prefetch_related('cities')
    serializer_class = CountrySerializer
    # permission_classes = (
    #     permissions.IsAuthenticated
    # )


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # permission_classes = (
    #     permissions.IsAuthenticated
    # )
    
