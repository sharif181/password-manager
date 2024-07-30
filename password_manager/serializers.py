from rest_framework import serializers

from users.serializers import CustomUserSerializer

from .models import PasswordStore


class PasswordStoreSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer()
    class Meta:
        model = PasswordStore
        fields = "__all__"