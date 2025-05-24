from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    """订单模型"""
    STATUS_CHOICES = [
        ('pending', '待处理'),
        ('processing', '处理中'),
        ('shipped', '已发货'),
        ('delivered', '已送达'),
        ('cancelled', '已取消'),
    ]
    
    PAYMENT_METHODS = [
        ('alipay', '支付宝'),
        ('wechat', '微信支付'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    name = models.CharField(max_length=100, verbose_name='收货人姓名', default='')
    phone = models.CharField(max_length=20, verbose_name='联系电话', default='')
    address = models.TextField(verbose_name='收货地址', default='')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='alipay', verbose_name='支付方式')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单总额')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='订单状态')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = '订单'
        verbose_name_plural = '订单'
    
    def __str__(self):
        return f'订单 #{self.id} - {self.user.username}'

class OrderItem(models.Model):
    """订单项模型"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='订单')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品')
    quantity = models.PositiveIntegerField(verbose_name='数量')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')
    
    class Meta:
        verbose_name = '订单项'
        verbose_name_plural = '订单项'
    
    @property
    def subtotal(self):
        return self.quantity * self.price
    
    def __str__(self):
        return f'{self.product.name} x {self.quantity}' 