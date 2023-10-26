from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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
    image = models.ImageField(
        upload_to='profile_image',
        blank=True
    )


    def login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('posts:index')
                else:
                    form.add_error(None, 'Неправильные почта или пароль')
        else:
            form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
    

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
