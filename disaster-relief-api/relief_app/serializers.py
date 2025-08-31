from rest_framework import serializers
from .models import Incident
from .models import Volunteer, PublicReport, ReliefItem, ReliefRequest
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


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = "__all__"


class PublicReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicReport
        fields = "__all__"



class ReliefItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliefItem
        fields = ["id", "name", "description", "quantity", "created_at"]


class ReliefRequestSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")  # auto use logged-in user
    item_name = serializers.ReadOnlyField(source="item.name") # show item name too

    class Meta:
        model = ReliefRequest
        fields = ["id", "user", "item", "item_name", "quantity_requested", "status", "created_at"]
        read_only_fields = ["status", "created_at"]