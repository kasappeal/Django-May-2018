from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response

from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer


class UsersAPI(GenericAPIView):

    queryset = User.objects.all()
    permission_classes = [UserPermission]

    def get_serializer_class(self):
        return UserSerializer if self.request.method == 'POST' else UserListSerializer

    def get(self, request):
        """
        Devuelve el listado de usuarios en formato JSON
        :param request: objeto de tipo HttpRequest
        :return: objeto Response con datos de los usuarios
        """
        queryset = self.queryset
        users = self.paginate_queryset(queryset)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(users, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        """
        Crea un usuario y devuelve la información del usuario creado
        :param request: objeto de tipo HttpRequest
        :return:  objeto Response con datos del usuario creado o 400 con los errores cometidos
        """
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(GenericAPIView):

    permission_classes = [UserPermission]

    def get(self, request, pk):
        """
        Devuelve el detalle del usuario con pk <pk>
        :param request: objeto de tipo HttpRequest
        :param pk: pk del usuario que queremos devolver
        :return: objeto Response con datos del usuario o 404
        """
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        """
        Borra el usuario con pk <pk> si existe.
        :param request: objeto de tipo HttpRequest
        :param pk: pk del usuario que queremos borrar
        :return: 204 o 404
        """
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        """
        Actualiza el usuario con pk <pk> si existe.
        :param request: objeto de tipo HttpRequest
        :param pk: pk del usuario que queremos actualizar
        :return: 202 si OK o 400 con errores
        """
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)