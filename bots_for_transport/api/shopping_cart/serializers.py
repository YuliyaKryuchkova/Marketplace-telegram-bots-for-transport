from api.bot.serializers import BotSerializer
from bot.serializers import BotSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from shopping_cart.models import Shopping_cart


class ShoppingCartSerializer(serializers.ModelSerializer):
    """Сериализатор для корзины покупок."""
    id = serializers.IntegerField()
    name = serializers.StringRelatedField(read_only=True)
    image = Base64ImageField()
    price = serializers.IntegerField()

    class Meta:
        model = Shopping_cart
        fields = ['user', 'bot']

    def to_representation(self, instance):
        return BotSerializer(instance.bot, context={
            'request': self.context.get('request')
        }).data
