from django.contrib.auth import authenticate, login as django_login, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render

from members.forms import MemberSignupForm, MemberProfileForm, UserProfileForm


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
            # TODO: Check if this is actually required. It may be handled by Django natively.
            if User.objects.filter(username=user.username).exists():
                return render(request, 'member_signup.html', {
                    'errors': {'Username': 'That username has already been taken.'},
                    'form': MemberSignupForm(request.POST)
                })

            user.save()

            member.user = user
            member.save()

            # Sign the user in and take them to the products page.
            django_login(request, user)
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

            # Load the user's cart into the session.
            cart = []
            for stored_cart_item in user.member.cartitem_set.all():
                cart.append({
                    "session_item_id": str(stored_cart_item.session_item_id),
                    "product_id": stored_cart_item.item.id,
                    "color": stored_cart_item.color.hex_value,
                    "size": stored_cart_item.size.name,
                    "quantity": stored_cart_item.quantity,
                })
            request.session['cart'] = cart

            return HttpResponseRedirect('/')
        else:
            return render(request, 'member_login.html', {
                'errors': {'User': 'The provided login credentials are invalid. Please try again.'}
            }, status=401)


def logout_view(request):
    """Logs a member out and returns them to the login screen."""
    logout(request)
    return login(request)


def profile(request):
    """Shows the member a profile screen with a form to edit details. POST requests will update
    the account."""
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        member_form = MemberProfileForm(
            request.POST, instance=request.user.member)

        if user_form.is_valid() and member_form.is_valid():
            user_form.save()
            member_form.save()

            # Sync the username and the email address
            request.user.email = user_form.cleaned_data['username']
            request.user.save()
        else:
            return render(request, 'member_profile.html', {
                'errors': {**user_form.errors, **member_form.errors},
                'user_form': UserProfileForm(request.POST, instance=request.user),
                'member_form': MemberProfileForm(request.POST, instance=request.user.member),
            })

    user_form = UserProfileForm(instance=request.user)
    member_form = MemberProfileForm(instance=request.user.member)
    return render(request, 'member_profile.html', {
        'user_form': user_form,
        'member_form': member_form
    })
