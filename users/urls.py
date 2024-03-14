from django.urls import path

from .views import get_signup_form, get_signin_form, signout, get_profile_page, edit_profile

urlpatterns = [
    path('signin_form/', get_signin_form, name='signin_form'),
    path('signup_form/', get_signup_form, name='signup_form'),
    path('signout/', signout, name='signout'),
    path('profile/', get_profile_page, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
