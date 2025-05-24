from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', '待支付'),
        ('paid', '已支付'),
        ('shipped', '已发货'),
        ('delivered', '已送达'),
        ('cancelled', '已取消'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户')
    status = models.CharField('订单状态', max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField('总金额', max_digits=10, decimal_places=2)
    shipping_address = models.TextField('收货地址')
    phone = models.CharField('联系电话', max_length=20)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '订单'
        verbose_name_plural = '订单'

    def __str__(self):
        return f'订单 {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='订单')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品')
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('数量', default=1)

    class Meta:
        verbose_name = '订单项'
        verbose_name_plural = '订单项'

    def __str__(self):
        return f'{self.quantity}x {self.product.name}'

    @property
    def total_price(self):
        return self.quantity * self.price
