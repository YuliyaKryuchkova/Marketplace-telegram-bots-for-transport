from rest_framework import serializers

from reviews.models import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reviews
        exclude = ('bot', )
