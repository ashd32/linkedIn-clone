from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Office
from .serializers import CompanySerializer, OfficeSerializer

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all().prefetch_related('offices')
    serializer_class = CompanySerializer
