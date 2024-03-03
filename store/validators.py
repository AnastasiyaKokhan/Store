from django.core.exceptions import ValidationError


def validate_letters(word):
    if not word.isalpha():
        raise ValidationError('название не должно содержать цифры')

def validate_price(number):
    if not number > 0:
        raise ValidationError('цена должна быть положительной')
