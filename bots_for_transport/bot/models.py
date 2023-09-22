from django.db import models
from categories.models import Category
from django.contrib.auth import get_user_model


User = get_user_model()


class Bot(models.Model):
    name = models.CharField(
        'Название',
        max_length=100
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    description = models.TextField(
        'Описание'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        null=True,
    )
    main_photo = models.ImageField(
        'Фото',
        upload_to='uploads/main/%Y/%m/%d/',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo_examples = models.ImageField(
        'Фото(образцы)',
        upload_to='uploads/examples/%Y/%m/%d/',
    )
    bot = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        verbose_name='Бот'
    )

    class Meta:
        ordering = ('bot',)
        verbose_name = 'Фото(образцы)'
        verbose_name_plural = 'Фото(образцы)'

    def __str__(self):
        return f' Фото бота {self.bot}'
