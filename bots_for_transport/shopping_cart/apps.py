from django.apps import AppConfig


class Shopping_cartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping_cart'
    verbose_name = 'Корзина'
    verbose_name_plural = 'Корзины'
