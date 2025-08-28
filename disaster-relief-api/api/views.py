from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .models import Incident, Volunteer, Report
from .serializers import IncidentSerializer, VolunteerSerializer, ReportSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsVolunteer, IsAdmin, IsPublic



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


# Public users can submit reports
class ReportCreateView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, IsPublic]

# Volunteers can update their availability
class VolunteerUpdateView(generics.UpdateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticated, IsVolunteer]

# Admins can view all reports
class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, IsAdmin]