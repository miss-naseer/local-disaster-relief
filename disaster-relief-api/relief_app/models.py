from django.db import models
from django.conf import settings
# Create your models here.
class Incident(models.Model):
    DISASTER_TYPES = [
        ('flood', 'Flood'),
        ('fire', 'Fire'),
        ('earthquake', 'Earthquake'),
        ('storm', 'Storm'),
        ('other', 'Other'),
    ]

    type = models.CharField(max_length=50, choices=DISASTER_TYPES)
    severity = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} at {self.location}"



# Volunteer model
class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    skills = models.TextField(help_text="List of skills (e.g., First Aid, Driving, Cooking)")
    availability = models.CharField(max_length=100, help_text="e.g., Weekends, Evenings")
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.skills})"


# Public Report model
class PublicReport(models.Model):
    REPORT_TYPES = [
        ('emergency', 'Emergency'),
        ('request', 'Request'),
        ('feedback', 'Feedback'),
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type.title()} - {self.name}"
