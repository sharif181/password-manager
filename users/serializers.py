from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ("groups", "user_permissions", "is_active", "is_staff", "is_superuser")
        extra_kwargs = {
            'password': {'write_only': True},
            'last_login': {"read_only": True},
            'date_joined': {"read_only": True},
        }
