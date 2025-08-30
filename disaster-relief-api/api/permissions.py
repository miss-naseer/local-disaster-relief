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


from rest_framework import permissions

class RoleBasedAccessPermission(permissions.BasePermission):
    """
    Custom permission to grant access based on the user's role.
    """

    def has_permission(self, request, view):
        # Anonymous users have no access
        if not request.user or not request.user.is_authenticated:
            return False  

        # Get user role from the UserProfile
        role = request.user.userprofile.role  

        # Example RBAC rules
        if role == "admin":
            return True  # Full access
        elif role == "volunteer":
            # Volunteers can only do SAFE_METHODS (GET, HEAD, OPTIONS)
            return request.method in permissions.SAFE_METHODS
        elif role == "donor":
            # Donors can view and create, but not delete or update
            return request.method in ["GET", "POST"]

        # Default: deny access
        return False
