from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.defaults import page_not_found

from post.models import Post
from reactions.forms import PostCommentForm
from .models import Comment, Vote

import json

@login_required()
def delete_comment(request, comment_pk):
    """
        retreve and delete a comment
    """
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect("post:details", pk=comment.post.pk)


@login_required()
def create_comment(request):

    if request.method == "POST":
        data = json.loads(request.body)

        comment = Comment(
            content=data.get("content"),
            author=request.user,
            post=Post.objects.get(pk=data.get("post_id"))
        )

        comment.save()

        response = {
            "pk": comment.pk,
            "content": comment.content,
            "author": comment.author.username,
            "created_at": comment.created_at.strftime("%b %d %Y, %I:%M %p"),
        }
        return JsonResponse(response)
    return page_not_found()


@login_required()
def update_vote(request):
    if request.method == "POST":
        data = json.loads(request.body)

        post = get_object_or_404(Post, id=data["post_id"])
        post.update_vote(author=request.user)

        all_votes = Vote.objects.filter(post=post)

        current_user_has_vote = False
        if request.user in [vote.user for vote in all_votes]:
            current_user_has_vote = True

        return JsonResponse({"vote_count": post.get_vote_count(), 
                             "current_user_has_vote": current_user_has_vote})
    return page_not_found()



