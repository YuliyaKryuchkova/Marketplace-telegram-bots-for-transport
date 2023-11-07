from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Модель пользователя."""
    SEX = (
        ('Male', 'Мужской'),
        ('Female', 'Женский')
    )
    email = models.EmailField(
        'Email',
        max_length=200,
        unique=True,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': "Пользователь с таким именем "
                      "пользователя уже существует.",
        },
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=128
    )
    confirm_password = models.CharField(
        verbose_name='Повторите пароль',
        max_length=128
    )
    image = models.ImageField(
        upload_to='profile_image',
        blank=True,
        null=True,
    )
    sex = models.CharField(
        'Пол',
        max_length=50,
        choices=SEX,
        blank=True,
        null=True
    )
    birthday = models.DateField(
        'Дата Рождения',
        blank=True,
        null=True
    )
    phone = PhoneNumberField(
        'Номер телефона',
        unique=True,
        blank=True,
        null=True
    )
    notifications_favorite = models.BooleanField(
        'Получать уведомления о товарах в избранном',
        default=False
    )
    notifications_discount = models.BooleanField(
        'Получать уведомления о скидках',
        default=False
    )


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()
        if self.username == 'me':
            raise ValidationError('Имя пользователя не может быть "me"')
        if User.objects.filter(email=self.email).exists():
            raise ValidationError('Пользователь с такой почтой уже существует')
