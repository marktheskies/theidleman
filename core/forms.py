from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )