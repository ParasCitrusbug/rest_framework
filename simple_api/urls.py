from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from simple_api.views import (
    StudentViews,
    StudentIDViews,
    SnippetsViews,
    SnippetDetails,
)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("basic/", StudentViews.as_view(), name="api_basic"),
    path("basic/<int:id>/", StudentIDViews.as_view(), name="api_basic_ID"),
    path("snippet/", SnippetsViews.as_view(), name="api_snippet"),
    path("snippet/<int:id>/", SnippetDetails.as_view(), name="api_snippet_detail"),
]
