from categories.models import Category
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Bot(models.Model):
    """Модель бота."""
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
    categories = models.ManyToManyField(
        Category,
        through='CategoryBot',
        related_name='bots',
        verbose_name='Категории',
    )
    main_photo = models.ImageField(
        'Фото',
        upload_to='uploads/main/%Y/%m/%d/',
    )
    price = models.DecimalField(
        'Цена',
        max_digits=8,
        decimal_places=0
    )
    is_special_offer = models.BooleanField(
        'Спецпредложение',
        default=False
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'

    def __str__(self):
        return self.name


class Photo(models.Model):
    """Модель фотографий примеров работы бота."""
    photo_examples = models.ImageField(
        'Фото(образцы)',
        upload_to='uploads/examples/%Y/%m/%d/',
    )
    bot = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        verbose_name='Бот',
        related_name='photo_examples'
    )

    class Meta:
        ordering = ('bot',)
        verbose_name = 'Фото(образцы)'
        verbose_name_plural = 'Фото(образцы)'

    def __str__(self):
        return f' Фото бота {self.bot}'


class CategoryBot(models.Model):
    """Модель категория/бот."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    bot = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        verbose_name='Бот'
    )

    class Meta:
        verbose_name = 'Категории бота'
        verbose_name_plural = 'Категории ботов'

    def __str__(self):
        return f'{self.category} {self.bot}'


class BotDiscount(models.Model):
    bot = models.OneToOneField(
        Bot,
        on_delete=models.CASCADE,
        related_name='discounts',
        verbose_name='Бот',
    )
    discount = models.DecimalField(
        'Скидка',
        max_digits=3,
        decimal_places=0,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Введите скидку от автора в процентах (от 0 до 100).'
    )

    class Meta:
        verbose_name = 'Скидка на бота'
        verbose_name_plural = 'Скидки на ботов'

    def __str__(self):
        return f'{self.bot.name}'
