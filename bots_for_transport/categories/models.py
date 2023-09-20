from django.db import models


class Category(models.Model):
    """Модель категории."""

    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Название категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория: {self.name}'
