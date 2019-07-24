from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from .models import City, Country
from .serializers import CountrySerializer, CitySerializer
from .pagination import LocationsResultSetPagination


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().prefetch_related('cities')
    serializer_class = CountrySerializer
    # permission_classes = (
    #     permissions.IsAuthenticated
    # )
   
    pagination_class = LocationsResultSetPagination



class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # permission_classes = (
    #     permissions.IsAuthenticated
    # )
    # pagination_class = LocationsResultSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('country',)
    
