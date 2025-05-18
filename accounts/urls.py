from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 用户个人资料
    path('profile/', views.profile, name='profile'),
    # 编辑个人资料
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    # 订单历史
    path('orders/', views.order_history, name='order_history'),
] 