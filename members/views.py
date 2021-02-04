from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render

from members.forms import MemberSignupForm


def signup(request):
    if request.method == 'GET':
        return render(request, 'member_signup.html', {
            'form': MemberSignupForm()
        })
    elif request.method == 'POST':
        form = MemberSignupForm(request.POST)

        if form.is_valid():
            member = form.save(commit=False)

            user = User(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
            )

            user.set_password(form.cleaned_data['password'])

            # Ensure the username is unique.
            if User.objects.filter(username=user.username).exists():
                return render(request, 'member_signup.html', {
                    'errors': {'Username': 'That username has already been taken.'},
                    'form': MemberSignupForm(request.POST)
                })

            user.save()

            member.user = user
            member.save()

            # TODO: Redirect to a "thanks for signing up" page.
            return HttpResponseRedirect('/products')

        else:
            return render(request, 'member_signup.html', {
                'errors': form.errors,
                'form': MemberSignupForm(request.POST)
            })


def login(request):
    if request.method != 'GET' and request.method != 'POST':
        return HttpResponseNotAllowed(['GET', 'POST'])

    if request.method == 'GET':
        return render(request, 'member_login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        print(user)

        if user is not None:
            django_login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'member_login.html', {
                'errors': {'User': 'The provided login credentials are invalid. Please try again.'}
            }, status=401)
