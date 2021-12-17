from rest_framework.permissions import BasePermission


class IsProfileOwner(BasePermission):
    """
    Allows access only to owners.
    """
    message = 'Editing profile is restricted to the owners only.'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
