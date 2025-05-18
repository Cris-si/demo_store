from django.shortcuts import render
from products.models import Product, Category

def home(request):
    products = Product.objects.filter(is_active=True)[:6]  # 只显示6个热门商品
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'products': products,
        'categories': categories,
    }) 