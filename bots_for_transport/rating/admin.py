from django.contrib import admin

from .models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Настройки для отображения рейтинга ботов в административной панели."""
    raw_id_fields = ('user', 'bot')
