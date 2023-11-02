from api.bot.serializers import BotSerializer
from rest_framework import serializers
from users.models import User

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


class ShoppingCartRetrieveSerializer(serializers.ModelSerializer):
    bot = serializers.SerializerMethodField()
    sum_price = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('confirm_password', 'email', 'password')

    # def get_sum_price(self, obj):
    #     return obj.in_shopping_cart.all().aggregate(Sum('bot__price'))

    def get_sum_price(self, obj):
        total_price = 0
        for item in obj.in_shopping_cart.all():
            bot_serializer = BotSerializer(item.bot)
            final_price = bot_serializer.data['final_price']
            total_price += final_price
        return total_price

    # def get_bot(self, obj):
    #     return obj.in_shopping_cart.all().values('bot__name', 'bot__price')

    def get_bot(self, obj):
        bot_data = []
        for item in obj.in_shopping_cart.all():
            bot_serializer = BotSerializer(item.bot)
            bot_data.append({
                'name': bot_serializer.data['name'],
                'price': bot_serializer.data['final_price'],
            })
        return bot_data
