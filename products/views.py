from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
    })

def product_detail(request, pk):
    return render(request, 'products/product_detail.html')

def product_by_category(request, category_id):
    return render(request, 'products/product_list.html')

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        
        # 处理分类
        category = self.request.GET.get('category')
        if category:
            category_mapping = {
                'furniture': '家具',
                'food': '食品',
                'baby': '母婴',
                'electronics': '电子产品'
            }
            if category in category_mapping:
                queryset = queryset.filter(category__name=category_mapping[category])
        
        # 处理排序
        sort = self.request.GET.get('sort')
        if sort == 'newest':
            queryset = queryset.order_by('-created_at')
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

