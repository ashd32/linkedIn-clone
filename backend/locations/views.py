from rest_framework import viewsets
from .models import City, Country
from .serializers import CountrySerializer, CitySerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all().prefetch_related('cities')
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer 
    
