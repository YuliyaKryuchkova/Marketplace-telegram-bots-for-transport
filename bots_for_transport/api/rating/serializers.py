from rest_framework import serializers

from rating.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Rating."""
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Rating
        exclude = ['bot', ]
