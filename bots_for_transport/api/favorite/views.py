from bot.models import Bot
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from favorite.models import Favorite
from .serializers import FavoriteSerializer


class FavoriteView(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request, id):
        data = {
            'user': request.user.id,
            'bot': id
        }
        bot = get_object_or_404(Bot, id=id)
        if not Favorite.objects.filter(
           user=request.user, bot=bot).exists():
            serializer = FavoriteSerializer(
                data=data, context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        bot = get_object_or_404(Bot, id=id)
        if Favorite.objects.filter(
           user=request.user, bot=bot).exists():
            Favorite.objects.filter(
                user=request.user, bot=bot
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
