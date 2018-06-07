from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from ads.models import Ad
from ads.serializers import AdListSerializer, AdDetailSerializer, NewAdSerializer


class AdListAPI(ListCreateAPIView):

    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return NewAdSerializer if self.request.method == 'POST' else AdListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MyAdsAPI(ListAPIView):

    serializer_class = AdListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(owner=self.request.user)
