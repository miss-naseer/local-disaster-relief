from django.urls import path, include
from .views import IncidentListCreateView, IncidentDetailView
from rest_framework.routers import DefaultRouter
from .views import VolunteerViewSet, PublicReportViewSet, ReliefItemListCreateView, ReliefRequestListCreateView

urlpatterns = [
    path('incidents/', IncidentListCreateView.as_view(), name='incident-list-create'),
    path('incidents/<int:pk>/', IncidentDetailView.as_view(), name='incident-detail'),
    path("items/", ReliefItemListCreateView.as_view(), name="relief-items"),
    path("requests/", ReliefRequestListCreateView.as_view(), name="relief-requests"),

]






router = DefaultRouter()
router.register(r'volunteers', VolunteerViewSet)
router.register(r'public-reports', PublicReportViewSet)
urlpatterns += [
    path('', include(router.urls)),
]