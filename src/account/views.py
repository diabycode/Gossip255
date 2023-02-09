from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth import urls


from .forms import UserForm
from .models import CustomUser


def signup_success(request):
    if request.user.is_authenticated:
        return redirect("post")
    return render(request, "account/signup_success.html")


class SignUp(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = "account/signup.html"
    success_url = reverse_lazy("account:signup_success")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("post:home")

        return super().get(request, *args, **kwargs)


class MyLoginView(LoginView):
    template_name = "account/login.html"
    success_url = reverse_lazy("post:home")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("post:home")

        return super(MyLoginView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return self.success_url


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("account:login")


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["posts"] = self.request.user.post_set.all().order_by("-create_on")

        return context

