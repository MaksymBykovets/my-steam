from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control bg-dark text-light border-secondary',
            'placeholder': 'Choose a username',
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control bg-dark text-light border-secondary',
            'placeholder': 'Enter your email',
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control bg-dark text-light border-secondary',
            'placeholder': 'Create a password',
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control bg-dark text-light border-secondary',
            'placeholder': 'Confirm your password',
        })