from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Конфигурация приложения Users."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'
