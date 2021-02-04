from django.urls import path
from members.views import signup, login, logout_view

urlpatterns = [
    path('signup', signup, name='member_signup'),
    path('login', login, name='member_login'),
    path('logout', logout_view, name='member_logout'),
]
