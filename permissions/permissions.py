from rest_framework import permissions
from rest_framework.views import Request
from users.models import User
from rest_framework.views import View


class IsAdmOrCreation(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.method == "POST" or request.user.is_superuser


class IsAdmOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            and request.user.is_authenticated
        )


class IsCriticOrAdm(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        if request.user.is_authenticated:
            return request.user.is_critic or request.user.is_superuser
        else:
            return request.method in permissions.SAFE_METHODS
