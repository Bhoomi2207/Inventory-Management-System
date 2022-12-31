from attr import field, fields
from django import forms
from django.contrib.auth.models import User
from .models import Product, Order
from user.models import Profile


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'order_quantity']


class StaffForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'groups', 'date_joined','user_permissions','phone',]
