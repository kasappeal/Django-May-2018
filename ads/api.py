from rest_framework.response import Response
from rest_framework.views import APIView

from ads.models import Ad
from ads.serializers import AdListSerializer


class AdListAPI(APIView):

    def get(self, request):
        """
        Devuelve la lista de anuncios
        :param request: objeto HttpRequest
        :return: objeto Response con resultado
        """
        ads = Ad.objects.all()
        serializer = AdListSerializer(ads, many=True)
        return Response(serializer.data)
