from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
        )
