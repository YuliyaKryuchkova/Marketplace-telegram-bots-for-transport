from django.contrib import admin

from .models import Bot, Photo


class PhotoAdmin(admin.TabularInline):
    model = Photo


class BotAdmin(admin.ModelAdmin):
    model = Bot
    inlines = [
        PhotoAdmin,
    ]


admin.site.register(Bot, BotAdmin)
