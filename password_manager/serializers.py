from rest_framework import serializers

from users.serializers import CustomUserSerializer

from .models import PasswordStore


class PasswordStoreSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    class Meta:
        model = PasswordStore
        fields = "__all__"
    

    def create(self, validated_data):
        request = self.context.get('request')
        password = PasswordStore.objects.create(owner=request.user, **validated_data)
        return password