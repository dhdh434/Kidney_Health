from django.urls import path
from .views import indexPageView, aboutPageView

urlpatterns = [
    path("about", aboutPageView, name="about"),
    path("", indexPageView, name="index"),
    
]
