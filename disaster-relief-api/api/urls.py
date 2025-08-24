from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncidentViewSet, VolunteerViewSet

router = DefaultRouter()
router.register(r'incidents', IncidentViewSet, basename='incident')
router.register(r'volunteers', VolunteerViewSet, basename='volunteer')

urlpatterns = [
    path('', include(router.urls)),
]
