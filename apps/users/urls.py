from rest_framework.urls import path
from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="user_login"),
]