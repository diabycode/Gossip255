from django.urls import path

from .views import PostHomeView

app_name = "post"

urlpatterns = [
    path('', PostHomeView.as_view(), name="home"),
]

