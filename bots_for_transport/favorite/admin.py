from django.contrib import admin

from .models import Favorite


@admin.register(Favorite)
class Favorite_admin(admin.ModelAdmin):
    list_display = ('bot', 'user')
    search_fields = ('bot', 'user')
    empty_value_display = '-пусто-'
