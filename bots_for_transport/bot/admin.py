from django.contrib import admin

from .models import Bot, BotDiscount, CategoryBot, Photo


class PhotoAdmin(admin.TabularInline):
    model = Photo


class BotAdmin(admin.ModelAdmin):
    model = Bot
    inlines = [
        PhotoAdmin,
    ]


class CategoryBotAdmin(admin.ModelAdmin):
    model = CategoryBot


class BotDiscountAdmin(admin.ModelAdmin):
    model = BotDiscount
    list_display = ('bot', 'discount')


admin.site.register(Bot, BotAdmin)
admin.site.register(CategoryBot)
admin.site.register(BotDiscount, BotDiscountAdmin)
