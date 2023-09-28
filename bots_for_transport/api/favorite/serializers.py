from bot.models import Bot
from rest_framework import serializers
from favorite.models import Favorite


class BotSortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bot
        fields = (
            'id',
            'name',
            'image',
            'price'
        )


class FavoriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favorite
        fields = ['user', 'bot']

    def to_representation(self, instance):
        return BotSortSerializer(instance.bot, context={
            'request': self.context.get('request')
        }).data
