from django.urls import path
from .views import get_page, get_add_product_page, get_product_description_page, get_products, get_test_form_page

urlpatterns = [
    path('', get_page, name='home'),
    path('add_product/', get_add_product_page, name='add_product'),
    path('product_description/<int:id>/', get_product_description_page, name='product_description'),
    path('products/<int:id>/', get_products, name='products'),
    path('test_form/', get_test_form_page),
]
