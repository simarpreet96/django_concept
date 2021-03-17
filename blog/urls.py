# from django.contrib import admin
from django.urls import path
# from .views import post_list, signup
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    # Post URL
    path('post_list/', views.post_list, name='post_list'),
    path('add_post/', views.add_post, name='add_post'),
    # Product URL
    path('product_list/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('filter_product/', views.filter_product, name='filter_product'),
    path('user_product/', views.user_product, name='user_product'),
    path('product_publish/<int:pk>', views.product_publish, name='product_publish'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product_del/<int:pk>/', views.product_del, name='product_del'),
    # Category URL
    path('category_list/', views.category_list, name='category_list'),
    path('category_product_list/<int:pk>/', views.category_product_list, name='category_product_list'),
    # wishlist URL
    path('add_to_wishlist/<int:pk>', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist_view/', views.wishlist_view, name='wishlist_view'),
    path('remove_wish/<int:pk>', views.remove_wish, name='remove_wish'),
    # add_to_cart URL
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('cart_view/', views.cart_view, name='cart_view'),
    path('delete_cart/<int:pk>/', views.delete_cart, name='delete_cart'),
    path('decreaseCart/<int:pk>/', views.decreaseCart, name='decreaseCart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name="payment"),
    # Store URL
    path('store_list/', views.store_list, name='store_list'),
    path('add_store/', views.add_store, name='add_store'),
    path('store_product_list/<int:pk>/', views.store_product_list, name='store_product_list'),
    path('signup/', views.signup, name='signup'),
    # path('login_view/', views.login_view, name='login_view'),
    # path('logout_view/', views.logout_view, name='logout_view'),
]
