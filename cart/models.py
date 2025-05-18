from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Cart(models.Model):
    """购物车"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = '购物车'

    def __str__(self):
        return f"{self.user.username}的购物车"

    @property
    def total_items(self):
        """计算购物车中的商品总数"""
        return sum(item.quantity for item in self.items.all())

    @property
    def total_price(self):
        """计算购物车总金额"""
        return sum(item.total_price for item in self.items.all())

class CartItem(models.Model):
    """购物车商品"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('数量', default=1)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '购物车商品'
        verbose_name_plural = '购物车商品'
        unique_together = ('cart', 'product')

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    @property
    def total_price(self):
        """计算小计金额"""
        return self.product.price * self.quantity

    def get_cost(self):
        return self.product.price * self.quantity 