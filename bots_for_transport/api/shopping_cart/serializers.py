from api.bot.serializers import BotSerializer
from rest_framework import serializers
from shopping_cart.models import Shopping_cart


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
    bot = BotSerializer()

    class Meta:
        model = Shopping_cart
        fields = '__all__'
