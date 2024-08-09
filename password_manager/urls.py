from django.urls import include, path

from .views import PasswordStoreViewSet

store_list = PasswordStoreViewSet.as_view({
    "get": "list"
})

store_post = PasswordStoreViewSet.as_view({
    "post": "create"
})

snippet_detail = PasswordStoreViewSet.as_view({
    "get": "retrieve",
    "patch": "partial_update",
    "delete": "destroy"
})



urlpatterns = [
    path("password-store/", include((
        [
            path("", store_list, name="password-store-list"),
            path("", store_post, name="password-store-create"),
            path("<int:pk>", snippet_detail, name="password-store-details"),
        ]
    )))
    
]