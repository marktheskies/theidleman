from django.views import generic
from django.shortcuts import render
from .models import Post

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def posts(request):
    context = {"post_list": Post.objects.all()}
    return render(request, "blog.html", context)

