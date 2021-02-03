from . import views
from django.urls import path
from blog.views import posts

urlpatterns = [
    path('', posts, name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]