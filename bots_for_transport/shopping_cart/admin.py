from django.contrib import admin

from .models import Shopping_cart


@admin.register(Shopping_cart)
class Shopping_cartAdmin(admin.ModelAdmin):
    list_display = ('bot', 'user')
    search_fields = ('bot', 'user')
    empty_value_display = '-пусто-'
