from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # 产品列表页
    path('', views.ProductListView.as_view(), name='product_list'),
    # 产品分类页
    path('category/<int:category_id>/', views.ProductListView.as_view(), name='product_list_by_category'),
    # 产品详情页
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
] 