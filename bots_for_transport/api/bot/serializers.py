from django.db.models import Avg

from bot.models import Bot, Photo
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from api.rating.serializers import RatingSerializer
from api.reviews.serializers import ReviewsSerializer


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo_examples',)


class BotSerializer(serializers.ModelSerializer):
    main_photo = Base64ImageField()
    is_special_offer = serializers.BooleanField(read_only=True)
    photo_examples = PhotoSerializer(many=True)
    author = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Bot
        fields = '__all__'


class BotReviewRatingSerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField()
    review = ReviewsSerializer(many=True)
    photo_examples = PhotoSerializer(many=True)
    author = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Bot
        exclude = ('is_special_offer', )

    def get_ratings(self, obj):
        return obj.ratings.aggregate(Avg('value'))
