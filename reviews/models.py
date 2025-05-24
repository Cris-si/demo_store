from django.db import models
from django.conf import settings
from products.models import Product

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1星'),
        (2, '2星'),
        (3, '3星'),
        (4, '4星'),
        (5, '5星'),
    ]
    
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, verbose_name='商品')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户')
    rating = models.IntegerField('评分', choices=RATING_CHOICES)
    comment = models.TextField('评价内容')
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)
    active = models.BooleanField('是否显示', default=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name = '商品评价'
        verbose_name_plural = '商品评价'
    
    def __str__(self):
        return f'{self.user.username}对{self.product.name}的评价'

class ReviewImage(models.Model):
    review = models.ForeignKey(Review, related_name='images', on_delete=models.CASCADE, verbose_name='评价')
    image = models.ImageField('图片', upload_to='reviews/%Y/%m/%d')
    
    class Meta:
        verbose_name = '评价图片'
        verbose_name_plural = '评价图片'
    
    def __str__(self):
        return f'{self.review.user.username}的评价图片' 