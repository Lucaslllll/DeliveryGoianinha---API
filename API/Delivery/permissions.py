from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # lê permissões são aceitas por qualquer requisição,
        # então nós iremos sempre aceitar requisições GET, HEAD ou OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # permissões de escrita são somente aceitas pelo dono do modelo.
        return obj.owner == request.user