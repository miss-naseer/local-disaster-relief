from django.shortcuts import render
from rest_framework import generics
from .models import Incident
from .serializers import IncidentSerializer

# List all incidents OR create a new one
class IncidentListCreateView(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


# Retrieve, update, or delete a single incident
class IncidentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
