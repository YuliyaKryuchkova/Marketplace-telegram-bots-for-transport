from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category."""
    bots = serializers.SerializerMethodField(
        method_name='get_bots'
    )

    class Meta:
        model = Category
        fields = ('name', 'bots', 'id')

    def get_bots(self, obj):
        category = obj
        return category.bots.values(
            'name',
            'author',
            'description',
            'categories',
            'main_photo',
            'price',
            'is_special_offer'
        )
