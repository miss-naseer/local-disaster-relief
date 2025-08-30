from rest_framework import serializers
from .models import Incident
from .models import UserProfile, Report, Assignment
from django.contrib.auth.models import User

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user",
            "role",
            "phone",
            "location",
            "skills",
            "availability",
        ]


class ReportSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Report
        fields = ["id", "title", "description", "created_by", "created_at"]


class AssignmentSerializer(serializers.ModelSerializer):
    report = ReportSerializer(read_only=True)
    volunteer = UserProfileSerializer(read_only=True)

    class Meta:
        model = Assignment
        fields = ["id", "report", "volunteer", "status", "assigned_at"]
