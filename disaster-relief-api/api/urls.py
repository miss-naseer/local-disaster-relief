from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IncidentViewSet, ReportViewSet, VolunteerViewSet, AssignmentViewSet,
    VolunteerDashboard, PublicDashboard,
    RegisterView, CustomTokenObtainPairView
)

router = DefaultRouter()
router.register(r'incidents', IncidentViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'volunteers', VolunteerViewSet)
router.register(r'assignments', AssignmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("volunteer-dashboard/", VolunteerDashboard.as_view(), name="volunteer-dashboard"),
    path("public-dashboard/", PublicDashboard.as_view(), name="public-dashboard"),
]
