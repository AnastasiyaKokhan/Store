from django import forms
from django.core.exceptions import ValidationError

from .models import Store, ProductColor, Product
from .validators import validate_letters


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=300, label='Название*', validators=[validate_letters])
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена*')
    description = forms.CharField(initial='нет описания', widget=forms.Textarea, label='Описание')
    colors = forms.ModelMultipleChoiceField(queryset=ProductColor.objects.all(), widget=forms.CheckboxSelectMultiple, label='Цвета*')
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
            'name': forms.TextInput(attrs={'class': 'name'}),
            'price': forms.NumberInput(attrs={'class': 'price'}),
            'description': forms.Textarea(attrs={'class': 'description'}),
            'colors': forms.CheckboxSelectMultiple(attrs={'class': 'colors'}),
            'image': forms.FileInput(attrs={'class': 'image'}),
            'store': forms.RadioSelect(attrs={'class': 'store'}),
        }
