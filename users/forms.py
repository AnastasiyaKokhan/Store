from django import forms
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    img = forms.ImageField(initial='no_user_photo.webp',
                           label='Фотография',
                           widget=forms.FileInput(attrs={'class': 'file'}))
    name = forms.CharField(label='Имя пользователя*',
                           widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(required=False,
                             label='Email',
                             widget=forms.EmailInput(attrs={'class': 'input'}))
    password1 = forms.CharField(label='Введите пароль*',
                                widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label='Повторите пароль*',
                                widget=forms.PasswordInput(attrs={'class': 'input'}))

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('пароли не совпадают')


class SignInForm(forms.Form):
    name = forms.CharField(label='Имя пользователя',
                           widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'input'}))
