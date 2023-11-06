import base64

from api.pagination import LimitPageNumberPagination
from api.permissions import IsAuthor, IsAuthorOrReadOnly
from django.core.files.base import ContentFile
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from bot.models import Bot, BotDiscount, Photo

from .serializers import BotReviewRatingSerializer, BotSerializer


class BotViewSet(ModelViewSet):
    """Вьюсет для бота.
    С возможностью пагинации, поиска по имени
    и описанию, фильтрации по категориям"""
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    pagination_class = LimitPageNumberPagination
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, )
    search_fields = ('name', 'description')
    permission_classes = (IsAuthorOrReadOnly, IsAuthor,)
    filterset_fields = ('categories', )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BotReviewRatingSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        discount_author = self.request.data.get("discount_author", 0)

        bot_instance = serializer.save(author=self.request.user)

        bot_discount, created = BotDiscount.objects.get_or_create(
            bot=bot_instance, defaults={"discount": discount_author}
        )

        # извлекает данные фотографии из данных запроса
        photos_data = self.request.data.get('photo_examples', None)
        if photos_data:
            # проход по каждой фотографии
            for photo_data in photos_data:
                photo_examples_data = photo_data.get('photo_examples', None)
                if photo_examples_data:
                    # создает новый экземпляр фотографии с помощью экземпляра
                    # бота
                    photo = Photo.objects.create(bot=bot_instance)
                    #  сохраняет данные photo_examples в экземпляре Photo
                    photo.photo_examples.save(
                        f"{photo.pk}.jpg",
                        ContentFile(base64.b64decode(
                            photo_examples_data.split(',')[1])),
                        save=True
                    )

        if not created:
            bot_discount.discount = discount_author
            bot_discount.save()
