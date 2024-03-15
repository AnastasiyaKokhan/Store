from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SignUpForm, SignInForm, EditForm
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
            birth = cd['birth_date']
            new_user = User.objects.create_user(username=username, email=email, password=password)
            Profile.objects.create(user=new_user, image=image, birth_date=birth)
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
            user = authenticate(username=username, password=password)
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


def get_profile_page(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    user = request.user
    form = EditForm(initial={'img': user.profile.image,
                             'name': user.username,
                             'birth_date': user.profile.birth_date,
                             'email': user.email})
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.image = form.cleaned_data['img']
            user.username = form.cleaned_data['name']
            user.profile.birth_date = form.cleaned_data['birth_date']
            user.email = form.cleaned_data['email']
            user = user.profile
            user.save()
            return redirect('profile')
    context = {
        "form": form,
    }
    return render(request, "update_form.html", context)
