from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .models import UserProfile


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


class SignInUser(AuthenticationForm):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateProfile(forms.ModelForm):
    date_of_birth = forms.DateField(label='Date Of Birth', required=True, widget=forms.TextInput(
        attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'gender', 'profile_pic']


class EditUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'gender', 'profile_pic']


class EditUser(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


