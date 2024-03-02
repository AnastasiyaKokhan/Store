from django.shortcuts import render, redirect

from .forms import AddProductForm, TestForm
from .models import Store, Product


# Create your views here.

def get_page(request):
    stores = Store.objects.all()
    products = Product.objects.all()
    context = {
        'stores': stores,
        'products': products,
    }
    return render(request, 'store.html', context)


def get_products(request, id):
    stores = Store.objects.all()
    products = Product.objects.filter(store_id=id)
    context = {
        'stores': stores,
        'products': products,
    }
    return render(request, 'store.html', context)


def get_product_description_page(request, id):
    stores = Store.objects.all()
    product = Product.objects.filter(id=id)
    colors = Product.objects.get(id=id).colors.all()
    context = {
        'stores': stores,
        'product': product,
        'colors': colors,
    }
    return render(request, 'product_description.html', context)


def get_add_product_page(request):
    stores = Store.objects.all()
    form = AddProductForm()
    context = {
        'stores': stores,
        'form': form,
    }
    if request.method == 'POST':
        form1 = AddProductForm(request.POST, request.FILES)
        colors = request.POST.get('colors')
        print(colors)
        if form1.is_valid():
            colors = form1.cleaned_data.pop('colors')
            new_product = Product(**form1.cleaned_data)
            new_product.save()
            new_product.colors.set(colors)
            return redirect('home')
        else:
            context['form'] = form1
            # print(form.errors)
        #     error = form.errors
        #     context['error'] = error

    return render(request, 'add_product.html', context)


def get_test_form_page(request):
    form = TestForm
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'test_form.html', context)
