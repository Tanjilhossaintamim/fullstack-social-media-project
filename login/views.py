from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .form import CreateNewUser, SignInUser, UpdateProfile, EditUserProfile, EditUser
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.


def signup(request):
    form = CreateNewUser()
    dic = {
        'form': form,
    }
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successfull !')
            dic.update({'form': form})
            return HttpResponseRedirect(reverse('login:signin'))
        else:
            dic.update({'failed': True})
    return render(request, 'login/signup.html', context=dic)


def signin(request):
    form = SignInUser()
    dic = {
        'form': form,
    }
    if request.method == 'POST':
        form = SignInUser(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('post_app:all_post'))

    return render(request, 'login/signin.html', context=dic)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:signin'))


@login_required
def update_user_profile(request):
    try:
        form = UpdateProfile()

        if request.method == 'POST':
            form = UpdateProfile(request.POST, request.FILES)
            if form.is_valid():
                user_form = form.save(commit=False)
                user_form.user = request.user
                user_form.save()
                return HttpResponseRedirect(reverse('login:profile'))
    except:
        messages.error(request, 'profile already updated !')

    return render(request, 'login/update_profile.html', context={'form': form})


@login_required
def user_profile(request):
    dic = {}

    return render(request, 'login/profile.html', context=dic)


@login_required
def edit_profile(request):
    current_user = request.user.user_profile
    form = EditUserProfile(instance=current_user)
    user_form = EditUser(instance=request.user)
    updated = False
    if request.method == 'POST':
        form = EditUserProfile(
            request.POST, request.FILES, instance=current_user)
        user_form = EditUser(request.POST, instance=request.user)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            form = EditUserProfile(instance=current_user)
            user_form = EditUser(instance=request.user)
            updated = True
    return render(request, 'login/edit_profile.html', context={'form': form, 'user_form': user_form, 'updated': updated})


@login_required
def password_change(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:profile'))
    return render(request, 'login/password_change.html', context={'form': form})


