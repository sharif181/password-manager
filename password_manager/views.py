from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import PasswordStore
from .serializers import PasswordStoreSerializer


class PasswordStoreViewSet(viewsets.ModelViewSet):
    queryset = PasswordStore.objects.all()
    serializer_class = PasswordStoreSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        password_store = PasswordStore.objects.filter(owner_id=self.request.user.id)
        return password_store