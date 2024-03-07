from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SignUpForm, SignInForm
from .models import Profile


# Create your views here.


def get_signup_form(request):
    signup_form = SignUpForm()
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST, request.FILES)
        if signup_form.is_valid():
            cd = signup_form.cleaned_data
            username = cd['name']
            email = cd['email']
            password = cd['password1']
            image = cd['img']
            new_user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile.objects.create(user=new_user, image=image)
            new_user = profile.user
            new_user.save()
            return redirect('signin_form')
    context = {
        'signup_form': signup_form
    }
    return render(request, 'signup_form.html', context)


def get_signin_form(request):
    signin_form = SignInForm()
    if request.method == 'POST':
        signin_form = SignInForm(request.POST)
        if signin_form.is_valid():
            cd = signin_form.cleaned_data
            username = cd['name']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup_form')
    context = {
        'signin_form': signin_form,
    }
    return render(request, 'signin_form.html', context)


def signout(request):
    logout(request)
    return redirect('home')
