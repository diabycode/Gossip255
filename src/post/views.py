from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from .forms import PostForm
from .models import Post


class PostHomeView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all().order_by("-create_on")
    template_name = "post/home.html"
    context_object_name = "posts"


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "post/create_post.html"
    success_url = reverse_lazy("account:profile")
    
    def form_valid(self, form):
        
        # setting author
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post/edit_post.html"
    form_class = PostForm
    success_url = reverse_lazy("account:profile")
    context_object_name = "post"

    def form_valid(self, form):
        form.instance.edited = True
        return super(EditPost, self).form_valid(form)


class PostDetails(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post/post_details.html"
    context_object_name = "post"


class DeletePost(LoginRequiredMixin, DeleteView):
    template_name = "post/post_delete_confirm.html"
    success_url = reverse_lazy("account:profile")
    model = Post
    context_object_name = "post"

