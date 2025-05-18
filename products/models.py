from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
import uuid
import os

User = get_user_model()

def generate_sku():
    """生成唯一的SKU编号"""
    return str(uuid.uuid4()).split('-')[0].upper()

def product_image_path(instance, filename):
    """生成商品图片的存储路径"""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('products', filename)

class Category(models.Model):
    """商品分类"""
    name = models.CharField('分类名称', max_length=100)
    description = models.TextField('描述', blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

class Brand(models.Model):
    """品牌模型"""
    name = models.CharField('品牌名称', max_length=100)
    slug = models.SlugField('URL别名', max_length=120, unique=True)
    logo = models.ImageField('品牌Logo', upload_to='brands/', null=True, blank=True)
    description = models.TextField('品牌描述', blank=True)
    website = models.URLField('官方网站', blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    """商品"""
    category = models.ForeignKey(Category, verbose_name='商品分类',
                               on_delete=models.CASCADE,
                               related_name='products')
    name = models.CharField('商品名称', max_length=200)
    description = models.TextField('商品描述')
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('库存', default=0)
    is_active = models.BooleanField('是否上架', default=True)
    image = models.ImageField('商品图片', upload_to=product_image_path, null=True, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.pk})

    @property
    def available(self):
        """商品是否可购买"""
        return self.is_active and self.stock > 0

    def get_image_url(self):
        """获取商品图片URL，如果没有图片则返回默认图片"""
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/images/no-image.png'

class ProductImage(models.Model):
    """商品图片"""
    product = models.ForeignKey(Product, verbose_name='商品',
                              on_delete=models.CASCADE,
                              related_name='images')
    image = models.ImageField('图片', upload_to=product_image_path)
    is_main = models.BooleanField('是否主图', default=False)
    created_at = models.DateTimeField('上传时间', auto_now_add=True)

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name
        ordering = ['-is_main', 'created_at']

    def __str__(self):
        return f"{self.product.name}的图片"

    def save(self, *args, **kwargs):
        """保存时如果是主图，则更新商品的image字段"""
        if self.is_main:
            self.product.image = self.image
            self.product.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """删除图片时同时删除文件"""
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

class ProductSpecification(models.Model):
    """商品规格模型"""
    category = models.ForeignKey(Category, verbose_name='商品分类',
                               on_delete=models.CASCADE,
                               related_name='specifications')
    name = models.CharField('规格名称', max_length=100)

    class Meta:
        verbose_name = '商品规格'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class ProductSpecificationValue(models.Model):
    """商品规格值模型"""
    product = models.ForeignKey(Product, verbose_name='商品',
                              on_delete=models.CASCADE,
                              related_name='specification_values')
    specification = models.ForeignKey(ProductSpecification, verbose_name='规格名称',
                                    on_delete=models.CASCADE,
                                    related_name='values')
    value = models.CharField('规格值', max_length=100)

    class Meta:
        verbose_name = '商品规格值'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.product.name} - {self.specification.name}: {self.value}"
