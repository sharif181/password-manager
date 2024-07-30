from django.urls import include, path

from .views import PasswordStoreViewSet

store_get = PasswordStoreViewSet.as_view({
    "get": "retrieve"
})

store_post = PasswordStoreViewSet.as_view({
    "post": "create"
})

store_update = PasswordStoreViewSet.as_view({
    "patch": "update"
})



urlpatterns = [
    path("password-store/", include((
        [
            path("<int:pk>", store_get, name="password-store-list"),
            path("", store_post, name="password-store-create"),
            path("<int:pk>", store_update, name="password-store-update"),
        ]
    )))
    
]