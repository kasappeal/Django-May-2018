from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario puede realizar la acción (GET, POST, PUT, DELETE) que quiere realizar sobre la vista <view>
        """
        from users.api import UserDetailAPI

        if request.method == 'POST':
            return True

        if request.user.is_authenticated and (
            request.method != 'GET' or request.user.is_superuser or isinstance(view, UserDetailAPI)
        ):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario puede realizar la acción sobre el objeto <obj>
        Un usuario puede borrar o actualizar un usuario, si es superusuario o si él mismo
        """
        return request.user.is_superuser or request.user == obj
