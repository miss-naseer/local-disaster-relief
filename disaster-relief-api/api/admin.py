from django.contrib import admin
from .models import Incident
from .models import Report, Assignment 
#Register your models here.

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "severity", "status", "location", "created_at")
    list_filter = ("type", "severity", "status", "location")
    search_fields = ("title", "description", "location", "reported_by")



admin.site.register(Report)

admin.site.register(Assignment)
