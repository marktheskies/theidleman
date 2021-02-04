from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.db import IntegrityError

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
                password=form.cleaned_data['password']
            )

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
