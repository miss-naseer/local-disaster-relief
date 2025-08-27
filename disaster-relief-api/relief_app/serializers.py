from rest_framework import serializers
from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = [
            "title",        # 1st
            "type",         # 2nd
            "severity",     # 3rd
            "location",     # 4th      
            "description",  # 5th
            "status "       # 6th
            "reported_by",  # 7th
            "reported_at",  #8th
        ]

        extra_kwargs = {
            "title": {"label": "Disaster Title"},
            "reported_by": {"label": "Reporter Name"},
            "severity": {"label": "Severity Level"},
        }
   # include all fields in the model can restrict later by fields = ['id', 'type', 'location', 'severity']
