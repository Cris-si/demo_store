from django.db import models
from django.conf import settings
from products.models import Product

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1星'),
        (2, '2星'),
        (3, '3星'),
        (4, '4星'),
        (5, '5星'),
    )

    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, verbose_name='商品')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户')
    rating = models.IntegerField('评分', choices=RATING_CHOICES)
    comment = models.TextField('评价内容')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '商品评价'
        verbose_name_plural = '商品评价'
        unique_together = ('product', 'user')

    def __str__(self):
        return f'{self.user.username}对{self.product.name}的评价'
