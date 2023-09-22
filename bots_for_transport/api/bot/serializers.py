from rest_framework.serializers import ModelSerializer
from bot.models import Bot
from drf_extra_fields.fields import Base64ImageField


class BotSerializer(ModelSerializer):
    main_photo = Base64ImageField()

    class Meta:
        model = Bot
        fields = '__all__'
