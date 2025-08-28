from django.contrib import admin
from .models import Incident
from .models import Volunteer, PublicReport
@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'severity', 'location', 'reported_at')
    search_fields = ('type', 'location', 'description')
    list_filter = ('type', 'severity', 'reported_at')
    ordering = ('-reported_at',)




@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "skills", "availability", "location")


@admin.register(PublicReport)
class PublicReportAdmin(admin.ModelAdmin):
    list_display = ("name", "report_type", "location", "created_at")
    list_filter = ("report_type", "created_at")
