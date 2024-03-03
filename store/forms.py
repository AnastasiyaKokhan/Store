from django import forms
from django.core.exceptions import ValidationError

from .models import Store, ProductColor, Product
from .validators import validate_letters, validate_price


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=300, validators=[validate_letters], label='Название*')
    price = forms.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price], label='Цена*')
    description = forms.CharField(initial='нет описания', widget=forms.Textarea, label='Описание')
    colors = forms.ModelMultipleChoiceField(queryset=ProductColor.objects.all(), widget=forms.CheckboxSelectMultiple,
                                            label='Цвета*')
    image = forms.ImageField(initial='no_photo.png', label='Фотография')
    store = forms.ModelChoiceField(queryset=Store.objects.all(), widget=forms.RadioSelect, label='Магазин*')

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if name != 'Johan':
    #         raise ValidationError('имя должно быть не Johan')
    #     else:
    #         name = 'Alice'
    #     return name


class TestForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'colors', 'image', 'store']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'price': forms.NumberInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'textarea'}),
            'colors': forms.CheckboxSelectMultiple(attrs={'class': 'choice'}),
            'image': forms.FileInput(attrs={'class': 'image'}),
            'store': forms.RadioSelect(attrs={'class': 'choice'}),
        }
        labels = {
            'name': 'Название',
            'price': 'Цена',
            'description': 'Описание',
            'colors': 'Цвета',
            'image': 'Фотография',
            'store': 'Магазин',
        }
