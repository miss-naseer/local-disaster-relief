from django.db import models

# Create your models here.
from django.db import models

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
