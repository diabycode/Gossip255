from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth import urls


from .forms import UserAuthenticationForm, UserSignUpForm
from .models import CustomUser


def signup_success(request):
    if request.user.is_authenticated:
        return redirect("post")
    return render(request, "account/signup_success.html")


class SignUp(CreateView):
    model = CustomUser
    form_class = UserSignUpForm
    template_name = "account/signup.html"
    success_url = reverse_lazy("account:signup_success")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if self.request.GET.get("next"):
                return self.request.GET.get("next")
            return redirect("post:home")

        return super().get(request, *args, **kwargs)


class MyLoginView(LoginView):
    template_name = "account/login.html"
    success_url = reverse_lazy("post:home")
    form_class = UserAuthenticationForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if self.request.GET.get("next"):
                return redirect(self.request.GET.get("next"))
            return redirect("post:home")

        return super(MyLoginView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.GET.get("next"):
            return self.request.GET.get("next")
        return self.success_url


class MyLogoutView(LogoutView):
    pass


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(CustomUser, username=self.kwargs.get("username"))
        context["posts"] = context["user"].post_set.all().order_by("-create_on")

        return context

