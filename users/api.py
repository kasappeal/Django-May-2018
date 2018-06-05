from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer, UserListSerializer


class UsersAPI(APIView):

    def get(self, request):
        """
        Devuelve el listado de usuarios en formato JSON
        :param request: objeto de tipo HttpRequest
        :return: objeto Response con datos de los usuarios
        """
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Crea un usuario y devuelve la información del usuario creado
        :param request: objeto de tipo HttpRequest
        :return:  objeto Response con datos del usuario creado o 400 con los errores cometidos
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):

    def get(self, request, pk):
        """
        Devuelve el detalle del usuario con pk <pk>
        :param request: objeto de tipo HttpRequest
        :param pk: pk del usuario que queremos devolver
        :return: objeto Response con datos del usuario o 404
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
