from django.urls import path

from blog.views import posts, post_detail

urlpatterns = [
    path('', posts, name='blog'),
    path('<slug:slug>/', post_detail, name='post_detail'),
]