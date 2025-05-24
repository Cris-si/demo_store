from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import CartItem

@login_required
def checkout(request):
    """结账页面"""
    cart_items = CartItem.objects.filter(cart__user=request.user)
    if not cart_items.exists():
        messages.warning(request, '您的购物车是空的')
        return redirect('cart:cart_detail')
    
    total_price = sum(item.total_price for item in cart_items)
    
    if request.method == 'POST':
        # 获取表单数据
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')
        
        # 创建订单
        order = Order.objects.create(
            user=request.user,
            name=name,
            phone=phone,
            address=address,
            payment_method=payment_method,
            total_price=total_price,
            status='pending'
        )
        
        # 创建订单项
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )
        
        # 清空购物车
        cart_items.delete()
        
        messages.success(request, '订单已创建成功！')
        return redirect('orders:order_success', order_id=order.id)
    
    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def order_success(request, order_id):
    """订单成功页面"""
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {
        'order': order
    })

@login_required
def order_history(request):
    """订单历史页面"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {
        'orders': orders
    }) 