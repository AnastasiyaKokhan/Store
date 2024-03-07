from django.urls import path

from .views import get_signup_form, get_signin_form, signout

urlpatterns = [
    path('signin_form/', get_signin_form, name='signin_form'),
    path('signup_form/', get_signup_form, name='signup_form'),
    path('signout/', signout, name='signout')
]
