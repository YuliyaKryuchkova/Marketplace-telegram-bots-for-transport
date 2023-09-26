from bot.models import Bot, Photo
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo_examples', )


class BotSerializer(serializers.ModelSerializer):
    main_photo = Base64ImageField()
    is_special_offer = serializers.BooleanField(read_only=True)
    photo_examples = PhotoSerializer(many=True)

    class Meta:
        model = Bot
        fields = '__all__'

