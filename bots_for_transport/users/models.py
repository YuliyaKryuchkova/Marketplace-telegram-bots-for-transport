from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.db import models


class User(models.Model):
    """Модель пользователя"""
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

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()
        if self.username == 'me':
            raise ValidationError('Имя пользователя не может быть "me"')
