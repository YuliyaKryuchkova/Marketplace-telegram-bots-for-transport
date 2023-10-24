from django.contrib import admin

from .models import Bot, CategoryBot, Photo


class PhotoAdmin(admin.TabularInline):
    """Настройки для отображения фотографий ботов в административной панели."""
    model = Photo


class BotAdmin(admin.ModelAdmin):
    """Настройки для отображения ботов в административной панели, включая отображение фотографий ботов."""
    model = Bot
    inlines = [
        PhotoAdmin,
    ]


class CategoryBotAdmin(admin.ModelAdmin):
    """Настройки для отображения категорий ботов в административной панели."""
    model = CategoryBot


admin.site.register(Bot, BotAdmin)
admin.site.register(CategoryBot)
