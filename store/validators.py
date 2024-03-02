from django.core.exceptions import ValidationError


def validate_letters(word):
    if not word.isalpha():
        raise ValidationError('можно вводить только буквы')
