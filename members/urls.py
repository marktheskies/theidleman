from django.urls import path
from members.views import signup

urlpatterns = [
    path('signup', signup, name='signup'),
]
