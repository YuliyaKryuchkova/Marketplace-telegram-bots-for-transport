from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from api.pagination import LimitPageNumberPagination
from bot.models import Bot
from api.permissions import IsAuthor, IsAuthorOrReadOnly
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
    filterset_fields = ('categories__name', )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BotReviewRatingSerializer
        return self.serializer_class
