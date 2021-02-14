from django import forms
from django.contrib.auth.models import User

from members.models import Member


class MemberSignupForm(forms.ModelForm):
    """A Model Form for the creation/update of a Member"""
    first_name = forms.CharField(max_length='150')
    last_name = forms.CharField(max_length='150')
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    # Add form-control class to all visible fields in the form.
    # Reference: Christian Abbott, 2015, https://stackoverflow.com/a/29717314
    def __init__(self, *args, **kwargs):
        super(MemberSignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-3'

    class Meta:
        model = Member
        fields = ('phone', 'address_street1', 'address_street2', 'address_suburb',
                  'address_state', 'address_country', 'address_postcode')
        labels = {
            'address_street1': 'Street Address 1',
            'address_street2': 'Street Address 2',
            'address_suburb': 'Suburb',
            'address_state': 'State',
            'address_country': 'Country',
            'address_postcode': 'Postcode',
        }


class MemberProfileForm(forms.ModelForm):

    # Add form-control class to all visible fields in the form.
    # Reference: Christian Abbott, 2015, https://stackoverflow.com/a/29717314
    def __init__(self, *args, **kwargs):
        super(MemberProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-3'

    class Meta:
        model = Member
        fields = ('phone', 'address_street1', 'address_street2', 'address_suburb',
                  'address_state', 'address_country', 'address_postcode')
        labels = {
            'address_street1': 'Street Address 1',
            'address_street2': 'Street Address 2',
            'address_suburb': 'Suburb',
            'address_state': 'State',
            'address_country': 'Country',
            'address_postcode': 'Postcode',
        }


class UserProfileForm(forms.ModelForm):

    # Add form-control class to all visible fields in the form.
    # Reference: Christian Abbott, 2015, https://stackoverflow.com/a/29717314
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-3'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
        labels = {'username': 'Email/Username'}
