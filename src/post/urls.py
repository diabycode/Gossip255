from django.urls import path

from .views import *

app_name = "post"

urlpatterns = [
    path('', PostHomeView.as_view(), name="home"),
    path('create/', CreatePost.as_view(), name="create"),
    path('<str:pk>/', PostDetails.as_view(), name="details"),
    path('<str:pk>/edit/', EditPost.as_view(), name="edit"),
    path('<str:pk>/delete/', DeletePost.as_view(), name="delete"),
    path("vote_status/<str:post_id>/", get_user_vote_status, name="vote_status"),
]

