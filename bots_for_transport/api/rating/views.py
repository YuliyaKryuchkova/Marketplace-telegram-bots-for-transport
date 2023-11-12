from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import action

from api.permissions import IsAuthor, IsAuthorOrReadOnly
from rating.models import Bot, Rating

from .serializers import RatingSerializer


class RatingCreateView(CreateAPIView,
                    UpdateModelMixin,
                    DestroyModelMixin):
    """Вью для создания, изменения, удаления рейтинга."""
    serializer_class = RatingSerializer
    permission_classes = (IsAuthor, IsAuthorOrReadOnly)


    def get_queryset(self, pk):
        return Rating.objects.filter(bot_id=pk)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        serializer.save(bot=get_object_or_404(Bot, id=pk), author=self.request.user)
