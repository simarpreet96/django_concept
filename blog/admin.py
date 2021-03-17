from django.contrib import admin
from .models import User, Post, Origin, Category, Product, Store, Productimage, Order, Cart, Wish, BillingAddress


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Origin)
admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Productimage)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Wish)
admin.site.register(BillingAddress)

# Register your models here.
