from django import forms
from members.models import Member
from django.contrib.auth.models import User


class MemberSignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length='150')
    last_name = forms.CharField(max_length='150')
    email = forms.EmailField()
    password = password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Member
        fields = ('phone', 'address_street1', 'address_street2', 'address_suburb',
                  'address_state', 'address_country', 'address_postcode')
