from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views import View
from django.views.defaults import page_not_found
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from reactions.forms import PostCommentForm
from .forms import PostForm
from .models import Post


class PostHomeView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all().order_by("-create_on")
    template_name = "post/home.html"
    context_object_name = "posts"


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "post/create_post.html"
    success_url = reverse_lazy("post:home")
    
    def form_valid(self, form):
        
        # setting author
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post/edit_post.html"
    form_class = PostForm
    # success_url = reverse_lazy("account:profile")
    context_object_name = "post"

    def dispatch(self, request, *args, **kwargs):
        post_object = self.model.objects.get(pk=self.kwargs.get("pk"))
        if request.user != post_object.author:
            return page_not_found(request=self.request, exception="Permission denied")
        return super(EditPost, self).dispatch(request, args, kwargs)

    def form_valid(self, form):
        form.instance.edited = True
        return super(EditPost, self).form_valid(form)
    
    def get_success_url(self):
        return reverse("post:details", kwargs={"pk": self.kwargs.get("pk")})


class PostDetails(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post/post_details.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = PostCommentForm
        context["comments"] = kwargs.get("object").comment_set.all().order_by("-created_at")
        return context


class DeletePost(LoginRequiredMixin, DeleteView):
    template_name = "post/post_delete_confirm.html"
    model = Post
    context_object_name = "post"

    def dispatch(self, request, *args, **kwargs):
        comment_object = self.model.objects.get(pk=self.kwargs.get("pk"))
        if request.user != comment_object.author:
            return page_not_found(request=self.request, exception="Permission denied")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("account:profile", kwargs={"username": self.request.user.username})


