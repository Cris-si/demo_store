from django.urls import path
from . import views

app_name = 'order_management'

urlpatterns = [
    # 创建订单
    path('create/', views.order_create, name='order_create'),
    # 订单详情
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    # 支付订单
    path('<int:order_id>/pay/', views.order_pay, name='order_pay'),
    # 取消订单
    path('<int:order_id>/cancel/', views.order_cancel, name='order_cancel'),
] 