from django.apps import AppConfig


class BotConfig(AppConfig):
    """Конфигурация приложения Bot."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'
    verbose_name = 'Бот'
    verbose_name_plural = 'Боты'
