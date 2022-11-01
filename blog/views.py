from turtle import title
from django.shortcuts import render
from blog.models import Configuracion
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

@login_required
def index(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'blog/index.html',{'configuracion':configuracion})

class ListPost(LoginRequiredMixin, ListView):
    model=Post

class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("list-post")
    
class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'

class SearchPostByName(ListView):#se agrega antes del listview el LoginRequiredMixin para filtrar el acceso con login
    def get_queryset(self):
        post_title= self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=post_title)