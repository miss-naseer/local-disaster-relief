from django.contrib import admin
from .models import Incident, Volunteer
# Register your models here.

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "severity", "status", "location", "created_at")
    list_filter = ("type", "severity", "status", "location")
    search_fields = ("title", "description", "location", "reported_by")

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "availability")
    list_filter = ("availability", "location")
    search_fields = ("name", "skills", "phone")
