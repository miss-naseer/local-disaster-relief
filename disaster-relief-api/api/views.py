from rest_framework import viewsets, filters, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Incident, Report, Assignment, UserProfile
from .serializers import (
    IncidentSerializer,
    ReportSerializer,
    AssignmentSerializer,
    UserProfileSerializer,
    UserSerializer,
    RegisterSerializer,
    CustomTokenObtainPairSerializer,
)
from .permissions import IsVolunteer, IsAdmin, IsPublic


# ---- Role Checks ----
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "admin"

def is_volunteer(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "volunteer"


# ---- Incident ----
class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all().order_by("-created_at")
    serializer_class = IncidentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["type", "severity", "status", "location", "title"]


# ---- Reports ----
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == "list":   # Only admins can list all reports
            return [permissions.IsAuthenticated(), IsAdmin()]
        if self.action == "create":  # Only public users can create reports
            return [permissions.IsAuthenticated(), IsPublic()]
        return super().get_permissions()


# ---- Volunteers ----
class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["update", "partial_update"]:  # Volunteers update their own profile
            return [permissions.IsAuthenticated(), IsVolunteer()]
        return super().get_permissions()


# ---- Assignments ----
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if is_admin(user):
            serializer.save()
        else:
            raise permissions.PermissionDenied("Only admins can assign tasks.")

    def perform_update(self, serializer):
        user = self.request.user
        assignment = self.get_object()

        if is_admin(user):
            serializer.save()  # Admins can reassign or change status
        elif is_volunteer(user) and assignment.volunteer.user == user:
            serializer.save()  # Volunteers update their own status
        else:
            raise permissions.PermissionDenied("Not allowed.")


# ---- Dashboards ----
class VolunteerDashboard(APIView):
    permission_classes = [permissions.IsAuthenticated, IsVolunteer]

    def get(self, request):
        return Response({"message": "Welcome, Volunteer!"})


class PublicDashboard(APIView):
    permission_classes = [permissions.IsAuthenticated, IsPublic]

    def get(self, request):
        return Response({"message": "Welcome, Public User!"})


# ==============================
# 🔹 Authentication (JWT)
# ==============================

# ---- Register ----
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# ---- Login (JWT) ----
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
