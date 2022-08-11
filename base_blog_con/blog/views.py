from django.shortcuts import render


def BlogHome(request):
    return render(request, "blog/home.html")
