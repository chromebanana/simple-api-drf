from django.urls import path
from .views import ListBookmarkView, LoginView, RegisterUsersView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('songs/', ListBookmarkView.as_view(), name="bookmarks-all"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register")
]