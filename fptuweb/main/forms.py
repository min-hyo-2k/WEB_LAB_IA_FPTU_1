from django import forms
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(email=email, password=password)

        if not user:
            raise forms.ValidationError('Invalid email or password')

        return cleaned_data
