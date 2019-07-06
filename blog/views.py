from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from .models import Post
from . import forms


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # django_specified : <app>/<model>_<viewtype>.html
    context_object_name = 'posts'     # django_specified : object
    ordering = ['-last_updated']
    paginate_by = 5


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_post.html' 
    context_object_name = 'posts'  
    paginate_by = 5

    def get_queryset(self):
        user =  get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-last_updated')


class PostDetailView(DetailView):
    model = Post


class PostCreateView (LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = forms.PostForm
    model = Post
    success_message = "%(title)s was created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    form_class = forms.PostForm
    model = Post
    success_message = "%(title)s was updated successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_home')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def post(self, request, *args, **kwargs):

        messages.error(request,'post is deleted')
        return super().post(self, request, *args, **kwargs)
