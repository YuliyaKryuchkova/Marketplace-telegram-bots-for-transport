from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from bot.models import Bot


User = get_user_model()


class Rating(models.Model):
    """Модель рейтинга."""
    bot = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name='Бот'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    value = models.IntegerField(
        verbose_name='Оценка',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
    )

    class Meta:
        unique_together = ('bot', 'user')
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'Оценка: {self.bot}'
