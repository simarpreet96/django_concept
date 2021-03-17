from django import forms
from .models import User, Post, Product, Category, Store, Productimage, BillingAddress
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('categoryname',)


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('storename', 'storeaddress',)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('author', 'name', 'price', 'description', 'category', 'store',)


class ProductimageForm(forms.ModelForm):
    class Meta:
        model = Productimage
        fields = ('product', 'image',)


class BillingForm(forms.ModelForm):

    class Meta:
        model = BillingAddress
        fields = ['address', 'zipcode', 'city', 'landmark']
