from django.db.models import Sum
from rest_framework import serializers

from api.bot.serializers import BotSerializer
from shopping_cart.models import Shopping_cart
from users.models import User


class ShoppingCartSerializer(serializers.ModelSerializer):
    """Сериализатор для корзины покупок."""

    class Meta:
        model = Shopping_cart
        fields = ['user', 'bot']

    def validate(self, data):
        user = data['user']
        if user.in_shopping_cart.filter(bot=data['bot']).exists():
            raise serializers.ValidationError(
                'Этот Bot уже находится в вашей корзине.'
            )
        return data

    def to_representation(self, instance):
        return BotSerializer(instance.bot, context={
            'request': self.context.get('request')
        }).data


class ShoppingCartListSerializer(serializers.ModelSerializer):
    bot = serializers.SerializerMethodField()
    sum_price = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('confirm_password', 'email', 'password')

    def get_sum_price(self, obj):
        return obj.in_shopping_cart.all().aggregate(Sum('bot__price'))

    def get_bot(self, obj):
        return obj.in_shopping_cart.all().values('bot__name', 'bot__price')