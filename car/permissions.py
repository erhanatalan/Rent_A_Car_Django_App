from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
)

class IsStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif (request.user.is_staff):
            return True
        else:
            return False