from rest_framework import serializers
from blog.models import User, Post, Category, Store, Product, Productimage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'id', 'url',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'id', 'url',)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('categoryname', 'slug', 'id', 'url',)


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ('storename', 'storeaddress', 'id', 'url',)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()
    store = StoreSerializer()

    class Meta:
        model = Product
        fields = ('author', 'name', 'price', 'description', 'category', 'store', 'id', 'url',)


class ProductimageSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Productimage
        fields = ('product', 'image', 'id', 'url',)
