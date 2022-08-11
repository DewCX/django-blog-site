from multiprocessing import context
from django.shortcuts import render
from .models import Post


def BlogHome(request):
    context = {
        "posts":Post.objects.all()
    }
    return render(request, "blog/home.html",context)


def BlogAbout(request):
    return render(request, "blog/about.html")