from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'severity', 'location', 'reported_at')
    search_fields = ('type', 'location', 'description')
    list_filter = ('type', 'severity', 'reported_at')
    ordering = ('-reported_at',)

from django.contrib import admin
from .models import Incident

 
