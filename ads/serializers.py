from rest_framework.serializers import ModelSerializer

from ads.models import Ad


class AdListSerializer(ModelSerializer):

    class Meta:

        model = Ad
        fields = '__all__'
