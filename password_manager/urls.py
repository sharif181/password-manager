from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'password-store', views.PasswordStoreViewSet, basename='password-store')

urlpatterns = [
    path("", include(router.urls))
]