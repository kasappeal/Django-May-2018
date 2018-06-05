from rest_framework import serializers


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()


class UserSerializer(UserListSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
