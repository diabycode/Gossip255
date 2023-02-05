from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import View


class PostHomeView(LoginRequiredMixin, View):
    login_url = reverse_lazy("account:login")

    def get(self, request):
        return render(request, "post/home.html")


