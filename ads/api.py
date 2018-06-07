from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.permissions import AdPermissions
from ads.serializers import AdListSerializer, AdDetailSerializer, NewAdSerializer


class AdViewSet(ModelViewSet):

    queryset = Ad.objects.all()
    permission_classes = [AdPermissions]

    def get_serializer_class(self):
        if self.action == 'create':
            return NewAdSerializer
        elif self.action == 'list':
            return AdListSerializer
        else:
            return AdDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class MyAdsAPI(ListAPIView):

    serializer_class = AdListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(owner=self.request.user)
