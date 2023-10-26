from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from api.permissions import IsAuthor, IsAuthorOrReadOnly
from .serializers import ReviewsSerializer
from bot.models import Bot
from reviews.models import Reviews


class ReviewCreateView(CreateAPIView,
                       UpdateModelMixin,
                       DestroyModelMixin):
    serializer_class = ReviewsSerializer
    permission_classes = (IsAuthor, IsAuthorOrReadOnly)

    def get_queryset(self, pk):
        return Reviews.objects.filter(bot_id=pk)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        serializer.save(author=self.request.user, bot=get_object_or_404(Bot, id=pk))
