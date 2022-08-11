from django.shortcuts import render
from django.http import HttpResponse

#First view

def home(request):
    return HttpResponse("<h1>Blog Home</h1>")
