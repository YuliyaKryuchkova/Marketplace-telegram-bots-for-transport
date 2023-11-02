from django.apps import AppConfig


class Shopping_cartConfig(AppConfig):
    """Конфигурация приложения Shopping_cart."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping_cart'
    verbose_name = 'Корзина'
    verbose_name_plural = 'Корзины'
