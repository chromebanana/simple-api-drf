from django.urls import path
from .views import ListSongView, LoginView, RegisterUsersView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('songs/', ListSongView.as_view(), name="songs-all"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register")
]