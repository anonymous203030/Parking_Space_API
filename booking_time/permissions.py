from django.contrib.auth.decorators import login_required
from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    """
    Allows access only to Managers
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profession == 'M'


class IsOwner(BasePermission):
    """
    Allow access only to owners
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
