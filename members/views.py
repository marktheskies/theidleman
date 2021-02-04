from django.shortcuts import render


def signup(request):
    return render(request, 'member_signup.html')
