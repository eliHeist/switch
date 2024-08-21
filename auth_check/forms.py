from django import forms

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="Username or Email", max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
