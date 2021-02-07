from django.urls import path
from members.views import signup, login, logout_view, profile

urlpatterns = [
    path('signup', signup, name='member_signup'),
    path('login', login, name='member_login'),
    path('logout', logout_view, name='member_logout'),
    path('profile', profile, name='member_profile'),
]
