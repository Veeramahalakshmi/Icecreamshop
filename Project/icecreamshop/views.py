from django.shortcuts import render, redirect, get_object_or_404
from .models import IceCream, CartItem

def homepage(request):
  return render(request,'icecreamshop/index.html')

def menu(request):
    ice_creams = IceCream.objects.all()
    return render(request, 'icecreamshop/menu.html', {'ice_creams': ice_creams})

def add_to_cart(request, ice_cream_id):
    ice_cream = get_object_or_404(IceCream, id=ice_cream_id)
    cart_item, created = CartItem.objects.get_or_create(ice_cream=ice_cream)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.all()
    return render(request, 'icecreamshop/cart.html', {'cart_items': cart_items})
