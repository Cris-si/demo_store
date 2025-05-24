from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Brand

@receiver(pre_save, sender=Brand)
def brand_pre_save(sender, instance, **kwargs):
    """自动生成品牌的slug"""
    if not instance.slug:
        instance.slug = slugify(instance.name) 