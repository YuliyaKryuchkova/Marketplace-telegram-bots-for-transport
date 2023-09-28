from categories.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category."""
    class Meta:
        model = Category
        fields = '__all__'
