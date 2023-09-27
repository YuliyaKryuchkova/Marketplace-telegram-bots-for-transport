from reviews.models import Reviews
from rest_framework import serializers


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Reviews
        exclude = ('bot', )