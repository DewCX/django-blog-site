from multiprocessing import context
from django.shortcuts import render
from .models import Post

#Working with class based views
from django.views.generic import ListView


# def BlogHome(request):
#     context = {
#         "posts":Post.objects.all()
#     }
#     return render(request, "blog/home.html",context)


def BlogAbout(request):
    return render(request, "blog/about.html")



#Class Based Views

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]