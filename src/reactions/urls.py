from django.urls import path

from .views import create_comment, update_vote

app_name = "reactions"

urlpatterns = [
    path('comment/', create_comment, name="comment"),
    path('update_vote/<str:post_pk>/', update_vote, name="update_vote"),
]
