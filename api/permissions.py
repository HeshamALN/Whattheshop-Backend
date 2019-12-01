from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "N3am 5air!!! Mo Salftek, Go Away"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.owner == request.user:
            return True
        return False