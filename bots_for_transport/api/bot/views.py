from api.pagination import LimitPageNumberPagination
from bot.models import Bot
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorOrReadOnly
from .serializers import BotSerializer


class BotViewSet(ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    pagination_class = LimitPageNumberPagination
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, )
    search_fields = ('name', 'description')
    permission_classes = (IsAuthorOrReadOnly, )
    filterset_fields = ('category', )
