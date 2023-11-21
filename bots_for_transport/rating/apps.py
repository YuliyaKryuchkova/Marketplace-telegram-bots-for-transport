from django.apps import AppConfig


class RatingConfig(AppConfig):
    """Конфигурация приложения Rating."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rating'
    verbose_name = 'Рейтинг'
    verbose_name_plural = 'Рейтинги'
