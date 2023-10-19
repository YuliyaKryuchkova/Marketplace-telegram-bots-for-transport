from django.contrib import admin

from .models import Bot, CategoryBot, Photo


class PhotoAdmin(admin.TabularInline):
    model = Photo


class BotAdmin(admin.ModelAdmin):
    model = Bot
    inlines = [
        PhotoAdmin,
    ]

class CategoryBotAdmin(admin.ModelAdmin):
    model = CategoryBot


admin.site.register(Bot, BotAdmin)
admin.site.register(CategoryBot)
