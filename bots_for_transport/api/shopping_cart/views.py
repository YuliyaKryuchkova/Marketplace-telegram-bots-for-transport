from api.pagination import LimitPageNumberPagination
from bot.models import Bot, User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsOwner
from shopping_cart.models import Shopping_cart
from .serializers import ShoppingCartRetrieveSerializer, ShoppingCartSerializer


class ShoppingCartRetrieveView(RetrieveAPIView):
    """Вью для получения корзины покупок пользователя."""
    serializer_class = ShoppingCartRetrieveSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class AddAndDeleteShoppingCartView(APIView):
    """Вью для добавления и удаления товаров из корзины покупок."""
    permission_classes = [IsAuthenticated, ]
    pagination_class = LimitPageNumberPagination

    def post(self, request, id):
        context = {'request': request}
        bot = get_object_or_404(Bot, id=id)
        data = {
            'user': request.user.id,
            'bot': bot.id
        }
        serializer = ShoppingCartSerializer(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        shopping_cart = Shopping_cart.objects.filter(
            user=request.user.id,
            bot=get_object_or_404(Bot, id=id)
        )
        shopping_cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
