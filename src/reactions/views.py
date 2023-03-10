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
def update_vote(request, post_pk):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_pk)
        post.update_vote(author=request.user)

        # return redirect('post:details', pk=post.id)
        return HttpResponse(post.vote_count)
    return page_not_found()



