from django.contrib import admin
from django.urls import path, include
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),

    #User authentication
    path('register/', account_views.register, name='register'),
]



