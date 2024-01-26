from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return super().has_permission

    def has_object_permission(self, request, view, obj):
        return obj.parent_list.user.pk == request.user.pk
