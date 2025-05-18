from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product

# Create your views here.

@login_required
def add_review(request, product_id):
    return redirect('products:product_detail', pk=product_id)

@login_required
def edit_review(request, review_id):
    return redirect('products:product_detail', pk=1)  # 临时使用固定值

@login_required
def delete_review(request, review_id):
    return redirect('products:product_detail', pk=1)  # 临时使用固定值

def product_reviews(request, product_id):
    return render(request, 'product_reviews/product_reviews.html')
