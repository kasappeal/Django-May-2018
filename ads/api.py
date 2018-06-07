from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from ads.models import Ad
from ads.serializers import AdListSerializer, AdDetailSerializer


class AdListAPI(ListCreateAPIView):

    queryset = Ad.objects.all()

    def get_serializer_class(self):
        return AdDetailSerializer if self.request.method == 'POST' else AdListSerializer


class AdDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
