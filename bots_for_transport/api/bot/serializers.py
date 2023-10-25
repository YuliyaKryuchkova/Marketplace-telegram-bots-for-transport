from django.db.models import Avg, Count
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from api.reviews.serializers import ReviewsSerializer
from bot.models import Bot, Photo


class PhotoSerializer(serializers.ModelSerializer):
    """Сериализатор примеров фото бота """
    class Meta:
        model = Photo
        fields = ('photo_examples',)


class BotSerializer(serializers.ModelSerializer):
    """Сериализатор списка ботов"""
    main_photo = Base64ImageField()
    is_special_offer = serializers.BooleanField(read_only=True)
    photo_examples = PhotoSerializer(many=True)
    author = serializers.StringRelatedField(read_only=True)
    categories = serializers.SerializerMethodField(
        method_name='get_categories'
    )

    class Meta:
        model = Bot
        fields = '__all__'

    def get_categories(self, obj):
        bot = obj
        return (
            bot.categories.values(
                'name',
            )
        )


class BotReviewRatingSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о боте.
    Включает расчет рейтинга бота и комментарии"""
    ratings = serializers.SerializerMethodField()
    review = ReviewsSerializer(many=True)
    photo_examples = PhotoSerializer(many=True)
    author = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    count_of_values = serializers.SerializerMethodField()

    class Meta:
        model = Bot
        fields = '__all__'

    def get_ratings(self, obj):
        return obj.ratings.aggregate(Avg('value'))

    def get_count_of_values(self, obj):
        return obj.ratings.values('value').annotate(count=Count('value'))
