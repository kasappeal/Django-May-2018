import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View


class UsersAPI(View):

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
        return HttpResponse(json.dumps(response))
