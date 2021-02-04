from django.urls import path
from members.views import signup, login

urlpatterns = [
    path('signup', signup, name='member_signup'),
    path('login', login, name='member_login'),
]
