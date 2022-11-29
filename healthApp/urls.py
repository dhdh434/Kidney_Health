from django.urls import path
from .views import indexPageView, aboutPageView, loginPageView, bootPageView

urlpatterns = [
    path("about", aboutPageView, name="about"),
    path("login", loginPageView, name="login"),
    path("boot", bootPageView, name="boot"),
    path("", indexPageView, name="index"),
    
]
