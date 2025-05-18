from django.db import migrations

def add_sample_products(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Product = apps.get_model('products', 'Product')
    
    # 创建分类
    electronics = Category.objects.create(name='电子产品')
    clothing = Category.objects.create(name='服装')
    
    # 创建商品
    Product.objects.create(
        category=electronics,
        name='iPhone 15 Pro',
        description='Apple最新旗舰手机',
        price=8999.00,
        stock=100,
        is_active=True
    )
    
    Product.objects.create(
        category=electronics,
        name='MacBook Pro 14',
        description='强大的专业级笔记本电脑',
        price=14999.00,
        stock=50,
        is_active=True
    )
    
    Product.objects.create(
        category=electronics,
        name='iPad Pro',
        description='专业级平板电脑',
        price=6999.00,
        stock=80,
        is_active=True
    )
    
    Product.objects.create(
        category=electronics,
        name='AirPods Pro',
        description='主动降噪无线耳机',
        price=1999.00,
        stock=200,
        is_active=True
    )
    
    Product.objects.create(
        category=clothing,
        name='T-Shirt',
        description='舒适休闲T恤',
        price=199.00,
        stock=500,
        is_active=True
    )
    
    Product.objects.create(
        category=clothing,
        name='Hoodie',
        description='时尚连帽卫衣',
        price=299.00,
        stock=300,
        is_active=True
    )
    
    Product.objects.create(
        category=clothing,
        name='Jeans',
        description='经典牛仔裤',
        price=399.00,
        stock=400,
        is_active=True
    )
    
    Product.objects.create(
        category=clothing,
        name='Casual Pants',
        description='休闲裤',
        price=299.00,
        stock=350,
        is_active=True
    )
    
    Product.objects.create(
        category=clothing,
        name='Sneakers',
        description='运动鞋',
        price=599.00,
        stock=250,
        is_active=True
    )

def remove_sample_products(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Category.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_products, remove_sample_products),
    ] 