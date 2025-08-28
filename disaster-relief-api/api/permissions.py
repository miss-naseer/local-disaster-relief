# api/permissions.py
from rest_framework.permissions import BasePermission

class IsVolunteer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.userprofile.role == 'volunteer'

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.userprofile.role == 'admin'

class IsPublic(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.userprofile.role == 'public'
