from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect("post:home")
    return render(request, "gossip225/index.html")

