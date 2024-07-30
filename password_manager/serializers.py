from rest_framework import serializers

from .models import PasswordStore


class PasswordStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordStore
        fields = "__all__"