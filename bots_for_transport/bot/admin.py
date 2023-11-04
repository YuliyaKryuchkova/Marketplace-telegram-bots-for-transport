from django.contrib import admin

from .models import BannerCategory, Bot, BotDiscount, CategoryBot, Photo


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


class BotDiscountAdmin(admin.ModelAdmin):
    model = BotDiscount
    list_display = ('bot', 'discount')


class BannerCategoryAdmin(admin.ModelAdmin):
    model = BannerCategory
    list_display = ('category', 'discount')


admin.site.register(Bot, BotAdmin)
admin.site.register(CategoryBot)
admin.site.register(BotDiscount, BotDiscountAdmin)
admin.site.register(BannerCategory, BannerCategoryAdmin)