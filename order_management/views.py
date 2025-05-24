from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def order_create(request):
    return render(request, 'order_management/order_create.html')

@login_required
def order_detail(request, order_id):
    return render(request, 'order_management/order_detail.html')

@login_required
def order_pay(request, order_id):
    return redirect('order_management:order_detail', order_id=order_id)

@login_required
def order_cancel(request, order_id):
    return redirect('order_management:order_detail', order_id=order_id)
