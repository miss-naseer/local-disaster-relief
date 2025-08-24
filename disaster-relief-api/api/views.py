from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Incident, Volunteer
from .serializers import IncidentSerializer, VolunteerSerializer
# Create your views here.

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all().order_by("-created_at")
    serializer_class = IncidentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["type", "severity", "status", "location", "title"]

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all().order_by("name")
    serializer_class = VolunteerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "skills", "location"]
