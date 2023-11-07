# Generated by Django 4.2.4 on 2023-11-07 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_shopping_cart', to='bot.bot', verbose_name='Боты в корзине покупок')),
            ],
            options={
                'verbose_name': 'Бот в корзине покупок',
                'verbose_name_plural': 'Боты в корзине покупок',
            },
        ),
    ]
