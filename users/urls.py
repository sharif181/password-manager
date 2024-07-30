from django.urls import include, path

# from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import UserViewSet

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')

user_details = UserViewSet.as_view({
    'get': 'retrieve'
})

user_create = UserViewSet.as_view({
    'post': 'create'
})

user_update = UserViewSet.as_view({
    'patch': 'partial_update'
})


urlpatterns = [
    path("users/", include((
        [
            path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
            path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
            path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
            path('', user_create, name="user_create"),
            path('<int:pk>', user_details, name="user_details"),
            path('<int:pk>/', user_update, name="user_update")
        ], 
    "users")
    ))
    # path("", include(router.urls)),
]