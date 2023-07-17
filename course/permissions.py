from rest_framework.permissions import BasePermission
from users.models import UserRoles
from rest_framework import permissions

class UserPermissionsModerator(permissions.BasePermission):

    message = 'Вы являетесь модератором...'

    def has_permission(self, request, view):
        if request.user.is_staff or request.user.role == UserRoles.MODERATOR:
            if view.action in ['list', 'retrieve', 'update', 'partial_update']:
                return True
        return False

class UserPermissionsOwner(permissions.BasePermission):
    message = 'Вы  вляетесь владельцем...'

    def has_permission(self, request, view):
        if request.user == obj.author:
            if view.action in ['list',  'retrieve', 'update', 'partial_update', 'destroy','create']:
                return True
        return False