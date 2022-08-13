from django.urls import path
from . import views

#Working with Class based views
from .views import PostListView, PostDetailView

urlpatterns = [
    # path("", views.BlogHome, name="blog-home"),
    path("about/", views.BlogAbout, name="blog-about"),

    #Working with class based views
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="blog-detail"),
]

