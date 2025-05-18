from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CartItem, Cart
from products.models import Product

@login_required
def cart_detail(request):
    """购物车详情页面"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    """添加商品到购物车"""
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    messages.success(request, f'已将 {product.name} 添加到购物车')
    return redirect('cart:cart_detail')

@login_required
def update_cart_item(request, item_id):
    """更新购物车商品数量"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, '购物车已更新')
    else:
        cart_item.delete()
        messages.success(request, '商品已从购物车中移除')
    
    return redirect('cart:cart_detail')

@login_required
def remove_from_cart(request, item_id):
    """从购物车中删除商品"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'已从购物车中移除 {product_name}')
    return redirect('cart:cart_detail') 