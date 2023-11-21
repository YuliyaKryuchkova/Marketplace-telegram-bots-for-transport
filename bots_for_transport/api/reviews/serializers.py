from rest_framework import serializers

from reviews.models import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Reviews."""
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reviews
        exclude = ['bot', ]
