from unicodedata import name
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'v1', views.ProductsApiviews)


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('all-products/<slug>', views.all_products, name='all-products'),
    path('product-category', views.product_category, name='product-category'),
    path('inside-category/<cat_id>', views.inside_category, name='inside-category'),
    path('api/', include(router.urls)),
]
