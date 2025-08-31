from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .serializers import IncidentSerializer 
from .models import Volunteer, PublicReport, Incident, ReliefItem, ReliefRequest
from .serializers import VolunteerSerializer, PublicReportSerializer , ReliefItemSerializer, ReliefRequestSerializer

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



# List + Create Relief Items
class ReliefItemListCreateView(generics.ListCreateAPIView):
    queryset = ReliefItem.objects.all()
    serializer_class = ReliefItemSerializer

# List + Create Relief Requests
# class ReliefRequestListCreateView(generics.ListCreateAPIView):
#     queryset = ReliefRequest.objects.all()
#     serializer_class = ReliefRequestSerializer
    
class ReliefRequestListCreateView(generics.ListCreateAPIView):
    queryset = ReliefRequest.objects.all()
    serializer_class = ReliefRequestSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)