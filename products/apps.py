from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    verbose_name = '商品管理'

    def ready(self):
        try:
            import products.signals  # noqa
        except ImportError:
            pass
