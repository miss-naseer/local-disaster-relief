from django.db import models
from django.conf import settings
# Create your models here.
class Incident(models.Model):
    STATUS_CHOICES = [
        ("reported", "Reported"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
    ]
    SEVERITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("critical", "Critical"),
    ]

    title = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=60)             # e.g., Flood, Fire
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    location = models.CharField(max_length=140)        # simple MVP location text
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="reported")
    reported_by = models.CharField(max_length=120, blank=True)  # name/email; MVP without auth
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.type})"



from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('public', 'Public User'),
        ('volunteer', 'Volunteer'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='public')

    # Volunteer-specific fields (only used if role = 'volunteer')
    phone = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=140, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)       # comma list or free text
    availability = models.BooleanField(default=True)       # available for tasks?

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Report(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reports"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="assignments")
    volunteer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="assignments")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report.title} → {self.volunteer.user.username} ({self.status})"
