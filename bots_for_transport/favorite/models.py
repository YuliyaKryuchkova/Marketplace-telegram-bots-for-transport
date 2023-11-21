from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

from bot.models import Bot

User = get_user_model()


class Favorite(models.Model):
    """Модель избранного"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь',
    )
    bot = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Бот в избранном',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            UniqueConstraint(fields=['user', 'bot'],
                             name='unique_favourite')
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.bot}" в Избранное'
