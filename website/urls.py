from django.urls import path
from .views import home_view, logout_view, register_view, post_view


app_name = "website"

urlpatterns = [
    path("", home_view, name="home"),
    path("logout/", logout_view, name="logout"),
    path("register", register_view, name="register"),
    path("post/", post_view, name="post"),
]
