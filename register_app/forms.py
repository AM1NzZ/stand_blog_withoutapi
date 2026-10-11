from django import forms
from django.core.validators import RegexValidator

password_validator = RegexValidator(
    regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d@$#%]{8,20}$",
    message="Must be 8-20 chars, with upper, lower, digit, and @$#!."
)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(label='Password',min_length=8,widget=forms.PasswordInput(attrs={'placeholder':'Create a password'}), validators=[password_validator])
    password2 = forms.CharField(label='Confirm Password',min_length=8,widget=forms.PasswordInput(attrs={'placeholder':'Repeat your password'}), validators=[password_validator])
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'placeholder':'example@gmail.com'}))
