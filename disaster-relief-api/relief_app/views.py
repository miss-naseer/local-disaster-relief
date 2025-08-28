from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import Incident
from .serializers import IncidentSerializer
from .models import Volunteer, PublicReport
from .serializers import VolunteerSerializer, PublicReportSerializer 

# List all incidents OR create a new one
class IncidentListCreateView(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


# Retrieve, update, or delete a single incident
class IncidentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Admins can do anything,
    others can only read.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        return request.method in permissions.SAFE_METHODS
    

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAdminOrReadOnly]





class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


class PublicReportViewSet(viewsets.ModelViewSet):
    queryset = PublicReport.objects.all()
    serializer_class = PublicReportSerializer

