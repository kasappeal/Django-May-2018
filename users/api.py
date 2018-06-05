from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView


class UsersAPI(APIView):

    def get(self, request):
        """
        Devuelve el listado de usuarios en formato JSON
        :param request: objeto de tipo HttpRequest
        :return: objeto de tipo Response
        """
        users = User.objects.all()
        response = []
        for user in users:
            response.append({
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
            })
        return Response(response)
