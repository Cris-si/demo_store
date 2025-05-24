from django.urls import path
from . import views

app_name = 'product_reviews'

urlpatterns = [
    # 添加评价
    path('add/<int:product_id>/', views.add_review, name='add_review'),
    # 编辑评价
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    # 删除评价
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    # 产品评价列表
    path('product/<int:product_id>/', views.product_reviews, name='product_reviews'),
] 