from api.pagination import LimitPageNumberPagination
from bot.models import Bot
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .serializers import BotSerializer


class BotViewSet(ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    pagination_class = LimitPageNumberPagination
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'description')
