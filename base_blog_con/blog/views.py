from multiprocessing import context
from django.shortcuts import render
from .models import Post

#Working with class based views
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def BlogHome(request):
#     context = {
#         "posts":Post.objects.all()
#     }
#     return render(request, "blog/home.html",context)


def BlogAbout(request):
    return render(request, "blog/about.html")



#Class Based Views

#Listing our post with ListView
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]

# DetailView
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

#CreateView
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

#Update View
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False