from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from api.permissions import IsAuthor, IsAuthorOrReadOnly
from bot.models import Bot
from reviews.models import Reviews

from .serializers import ReviewsSerializer


class ReviewCreateView(CreateAPIView,
                       UpdateModelMixin,
                       DestroyModelMixin):
    """Вью для создания, изменения, удаления отзывов."""
    serializer_class = ReviewsSerializer
    permission_classes = (IsAuthor, IsAuthorOrReadOnly)

    def get_queryset(self, pk):
        return Reviews.objects.filter(bot_id=pk)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        serializer.save(author=self.request.user, bot=get_object_or_404(Bot, id=pk))
