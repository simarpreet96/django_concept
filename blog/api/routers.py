from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api.viewsets import UserViewSet, PostViewSet, CategoryViewSet, StoreViewSet, ProductViewSet,\
    ProductimageViewSet, HelloView
from blog.api import viewsets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'users', viewsets.UserViewSet)
router.register(r'posts', viewsets.PostViewSet)
router.register(r'categories', viewsets.CategoryViewSet)
router.register(r'stores', viewsets.StoreViewSet)
router.register(r'products', viewsets.ProductViewSet)
router.register(r'productsimages', viewsets.ProductimageViewSet)


# API endpoints
urlpatterns = format_suffix_patterns([
    path('', include(router.urls)),
    path('hello/', viewsets.HelloView.as_view(), name='hello'),
])
urlpatterns += router.urls
