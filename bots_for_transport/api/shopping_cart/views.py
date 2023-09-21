from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from bot.models import Bot
from shopping_cart.models import Shopping_cart
from shopping_cart.serializers import Shopping_cartSerializer


class Shopping_cartView(APIView):
    """Добавление рецепта в корзину или его удаление."""

    permission_classes = [IsAuthenticated, ]

    def post(self, request, id):
        data = {
            'user': request.user.id,
            'bot': id
        }
        bot = get_object_or_404(Bot, id=id)
        if not Shopping_cart.objects.filter(
           user=request.user, bot=bot).exists():
            serializer = Shopping_cartSerializer(
                data=data, context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        bot = get_object_or_404(Bot, id=id)
        if Shopping_cart.objects.filter(
           user=request.user, bot=bot).exists():
            Shopping_cart.objects.filter(
                user=request.user, bot=bot
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
