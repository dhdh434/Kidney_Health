from django.urls import path
from .views import indexPageView, aboutPageView, loginPageView, bootPageView, createAccPageView

urlpatterns = [
    path("about/", aboutPageView, name="about"),
    path("login/", loginPageView, name="login"),
    path("createacc/", createAccPageView, name="createAcc"),
    path("boot/", bootPageView, name="boot"),
    path("", indexPageView, name="index"),
    
]
