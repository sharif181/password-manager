from django.urls import include, path

from .views import PasswordStoreViewSet

store = PasswordStoreViewSet.as_view({
    "get": "list",
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
            path("", store, name="password-store"),
            path("<int:pk>", snippet_detail, name="password-store-details"),
        ]
    )))
    
]