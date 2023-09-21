from bot.models import Bot
from rest_framework import serializers
from shopping_cart.models import Shopping_cart


class BotShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bot
        fields = (
            'id',
            'name',
            'image',
            'price'
        )


class ShoppingCartSerializer(serializers.ModelSerializer):
    """Сериализатор для корзины покупок."""

    class Meta:
        model = Shopping_cart
        fields = ['user', 'bot']

    def to_representation(self, instance):
        return BotShortSerializer(instance.bot, context={
            'request': self.context.get('request')
        }).data
