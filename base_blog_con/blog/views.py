from multiprocessing import context
from django.shortcuts import render
from .models import Post

#Working with class based views
from django.views.generic import ListView, DetailView, CreateView



# def BlogHome(request):
#     context = {
#         "posts":Post.objects.all()
#     }
#     return render(request, "blog/home.html",context)


def BlogAbout(request):
    return render(request, "blog/about.html")



#Class Based Views

#Listing our post with ListView
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]

# DetailView
class PostDetailView(DetailView):
    model = Post

#CreateView
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)