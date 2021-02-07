from django.views import generic
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm

def posts(request):
    context = {"post_list": Post.objects.all()}
    return render(request, "blog.html", context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {"post_detail": post, "form": CommentForm()}

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect ("post_detail", slug=post.slug)

    return render(request, "post_detail.html", context)