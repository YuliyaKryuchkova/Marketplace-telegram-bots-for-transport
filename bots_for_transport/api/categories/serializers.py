from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category."""
    class Meta:
        model = Category
        fields = '__all__'
