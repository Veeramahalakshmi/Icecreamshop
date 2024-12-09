from django.urls import path
from . import views

urlpatterns = [
  path('',views.homepage, name=" "),
     path('menu/', views.menu, name='menu'),
    path('add_to_cart/<int:ice_cream_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
]