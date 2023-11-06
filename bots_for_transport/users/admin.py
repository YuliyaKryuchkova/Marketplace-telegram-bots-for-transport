from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройки для отображения модели пользователей в административной
    панели."""
    fieldsets = (
        (
            'Данные пользователя',
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password',
                    'image',
                    'is_author',
                )
            }
        ),
        ('Права пользователя', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
        )}),
    )
    add_fieldsets = (

    )

    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_author',
    )
    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )
    list_filter = (
        'email',
        'first_name',
        'is_author',
    )
    empty_value_display = '-пусто-'


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
