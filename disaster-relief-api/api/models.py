from django.db import models

# Create your models here.
from django.db import models

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


class Volunteer(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=140)
    skills = models.TextField(blank=True)              # comma list or free text (MVP)
    availability = models.BooleanField(default=True)   # available for tasks?

    def __str__(self):
        return self.name
