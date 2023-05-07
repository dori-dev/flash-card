from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_authenticated and
            request.user
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            obj.user == request.user
        )
