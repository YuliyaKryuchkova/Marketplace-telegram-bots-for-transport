import math

from api.reviews.serializers import ReviewsSerializer
from categories.models import Category
from django.db.models import Avg, Count, Max
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from bot.models import BannerCategory, Bot, BotDiscount, Photo


class PhotoSerializer(serializers.ModelSerializer):
    """Сериализатор примеров фото бота"""
    photo_examples = Base64ImageField()

    class Meta:
        model = Photo
        fields = ('photo_examples',)


class CategoryNameSerializer(serializers.PrimaryKeyRelatedField):
    """
    Класс сериализатора (переопределённый), представляющий имя категории
    для данного значения первичного ключа.
    """
    def to_representation(self, value):
        return value.name


class AbstractBotSerializer(serializers.ModelSerializer):
    """
    Абстрактный класс, который определяет поведение сериализации и
    десериализации для данных, связанных с ботами.
    """
    author = serializers.StringRelatedField(read_only=True)
    photo_examples = PhotoSerializer(many=True, read_only=True)
    discount_author = serializers.SerializerMethodField()
    discount_category = serializers.SerializerMethodField(required=False)
    amount_discounts_sum = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()
    categories = CategoryNameSerializer(
        required=False,
        queryset=Category.objects.all(),
        many=True,
    )

    class Meta:
        abstract = True
        fields = '__all__'

    def get_discount_author(self, obj):
        return math.ceil(obj.discounts_author.discount) if hasattr(
            obj, 'discounts_author') else 0

    def get_discount_category(self, obj):
        """Расчёт скидки по категории бота"""
        try:
            category_id = self.context['request'].query_params.get(
                'categories')
            if category_id:
                # Получаем скидку для указанной категории
                banner_category = BannerCategory.objects.get(
                    category_id=category_id)
                discount = banner_category.discount
            else:
                # Получаем скидки для категорий, к которым относится бот
                discounts = BannerCategory.objects.filter(
                    id__in=obj.categories.values_list('id', flat=True),
                    discount__isnull=False
                )
                if discounts.exists():
                    discount = discounts.aggregate(Max('discount'))[
                        'discount__max']
                else:
                    # Если категорий со скидками нет, то устанавливаем скидку 0
                    discount = 0
        except BannerCategory.DoesNotExist:
            discount = 0
        if discount is None or not obj.categories.exists():
            discount = 0
        if obj.categories.count() == 1 and hasattr(obj.categories.first(),
                                                   'discounts_category'):
            discount = obj.categories.first().discounts_category.discount
        return math.ceil(discount)

    def get_amount_discounts_sum(self, obj):
        """Суммирование скидки от автора и по категории."""
        try:
            discount_author = obj.discounts_author.discount
        except BotDiscount.DoesNotExist:
            discount_author = 0
        discount_category = self.get_discount_category(obj)
        return math.ceil(discount_author + discount_category)

    def get_final_price(self, obj):
        """Вычисление итоговой цены бота с учётом всех скидок."""
        try:
            discount_author = obj.discounts_author.discount
        except BotDiscount.DoesNotExist:
            discount_author = 0
        discount_category = self.get_discount_category(obj)
        total_discount = discount_author + discount_category
        if total_discount >= 100:
            return 1
        else:
            return math.ceil(obj.price - (obj.price * total_discount / 100))


class BotSerializer(AbstractBotSerializer):
    """Сериализатор списка ботов"""
    main_photo = Base64ImageField()
    is_special_offer = serializers.BooleanField(read_only=True)

    class Meta(AbstractBotSerializer.Meta):
        model = Bot
        fields = '__all__'


class BotReviewRatingSerializer(AbstractBotSerializer):
    """Сериализатор для детальной информации о боте.
    Включает расчет рейтинга бота и комментарии"""
    ratings = serializers.SerializerMethodField()
    review = ReviewsSerializer(many=True)
    count_of_values = serializers.SerializerMethodField()

    class Meta(AbstractBotSerializer.Meta):
        model = Bot
        fields = '__all__'

    def get_ratings(self, obj):
        return obj.ratings.aggregate(Avg('value'))

    def get_count_of_values(self, obj):
        return obj.ratings.values('value').annotate(count=Count('value'))
