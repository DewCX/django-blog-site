from django.urls import path
from . import views

#Working with Class based views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    # path("", views.BlogHome, name="blog-home"),
    path("about/", views.BlogAbout, name="blog-about"),

    #Working with class based views
    path("", PostListView.as_view(), name="blog-home"),
    path("post/new", PostCreateView.as_view(), name="blog-new"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="blog-detail"), 
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="blog-update"), 
]

