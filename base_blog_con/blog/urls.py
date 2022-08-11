from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogHome, name="blog-home"),
    path("about/", views.BlogAbout, name="blog-about")
]

