from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class UsersAPI(APIView):

    def get(self, request):
        """
        Devuelve el listado de usuarios en formato JSON
        :param request: objeto de tipo HttpRequest
        :return: objeto de tipo Response
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
