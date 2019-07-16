from rest_framework.permissions import (
    AllowAny, BasePermission, IsAdminUser, IsAuthenticated
)
from rest_action_permissions.permissions import ActionPermission


class IsAccountOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class AccountPermissions(ActionPermission):
    create_perms = IsAuthenticated
    retrieve_perms = IsAuthenticated
    update_perms = IsAccountOwner
    delete_perms = IsAccountOwner
    list_perms = IsAuthenticated
    read_perms = AllowAny