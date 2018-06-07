from rest_framework.generics import ListAPIView, RetrieveAPIView

from ads.models import Ad
from ads.serializers import AdListSerializer, AdDetailSerializer


class AdListAPI(ListAPIView):

    queryset = Ad.objects.all()
    serializer_class = AdListSerializer


class AdDetailAPI(RetrieveAPIView):

    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer

