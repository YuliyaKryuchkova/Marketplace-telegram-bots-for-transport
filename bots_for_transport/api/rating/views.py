from rest_framework import viewsets
from rating.models import Bot, Rating
from .serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        bot_id = self.kwargs.get('bot_id')
        bot = Bot.objects.get(id=bot_id)
        serializer.save(bot=bot, user=self.request.user)
