from django.urls import path

from .views import create_comment, update_vote, delete_comment

app_name = "reactions"

urlpatterns = [
    path('comment/', create_comment, name="comment"),
    path('comment/<str:comment_pk>/delete/', delete_comment, name="delete_comment"),
    path('update_vote/<str:post_pk>/', update_vote, name="update_vote"),
]
