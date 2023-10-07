from rest_framework import serializers

from api.bot.serializers import BotSerializer
from favorite.models import Favorite
from users.models import User


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


class FavoriteRetrieveSerializer(serializers.ModelSerializer):
    bot = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('confirm_password', 'email', 'password')

    def get_bot(self, obj):
        return obj.favorites.all().values('bot__name', 'bot__price')


class FavoriteListSerializer(serializers.ModelSerializer):
    bot = BotSerializer()

    class Meta:
        model = Favorite
        fields = '__all__'
