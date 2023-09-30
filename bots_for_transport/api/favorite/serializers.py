from api.bot.serializers import BotSerializer
from rest_framework import serializers
from favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favorite
        fields = ['user', 'bot']

    def validate(self, data):
        user = data['user']
        if user.favorites.filter(bot=data['bot']).exists():
            raise serializers.ValidationError(
                'Этот Bot уже находится в списке избранного.'
            )
        return data

    def to_representation(self, instance):
        return BotSerializer(instance.bot, context={
            'request': self.context.get('request')
        }).data



class FavoriteListSerializer(serializers.ModelSerializer):
    bot = BotSerializer()

    class Meta:
        model = Favorite
        fields = '__all__'