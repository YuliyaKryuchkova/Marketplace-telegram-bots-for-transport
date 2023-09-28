from api.bot.serializers import BotSerializer
from rest_framework import serializers
from shopping_cart.models import Shopping_cart


class ShoppingCartSerializer(serializers.ModelSerializer):
    """Сериализатор для корзины покупок."""

    class Meta:
        model = Shopping_cart
        fields = ['user', 'bot']

    def to_representation(self, instance):
        return BotSerializer(instance.bot, context={
            'request': self.context.get('request')
        }).data
