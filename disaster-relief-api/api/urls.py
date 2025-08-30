from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncidentViewSet

from .views import (
    ReportViewSet,
    VolunteerViewSet,
    AssignmentViewSet,
    VolunteerDashboard,
    PublicDashboard,
)

router = DefaultRouter()
router.register(r'incidents', IncidentViewSet, basename='incident')
router.register(r'volunteers', VolunteerViewSet, basename='volunteer')
router.register(r'reports', ReportViewSet, basename="report")
router.register(r'assignments', AssignmentViewSet, basename="assignment")

urlpatterns = [
    path('', include(router.urls)),
]



urlpatterns = [
    path('api/', include(router.urls)),

    # Custom dashboards
    path('api/dashboard/volunteer/', VolunteerDashboard.as_view(), name='volunteer-dashboard'),
    path('api/dashboard/public/', PublicDashboard.as_view(), name='public-dashboard'),
]
