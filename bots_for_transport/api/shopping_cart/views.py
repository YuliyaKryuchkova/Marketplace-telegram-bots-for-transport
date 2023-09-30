from api.pagination import LimitPageNumberPagination
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from shopping_cart.models import Shopping_cart
from .serializers import ShoppingCartSerializer, ShoppingCartListSerializer
from bot.models import Bot


class ShoppingCartListView(ListAPIView):
    serializer_class = ShoppingCartListSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Shopping_cart.objects.filter(user=user)

    def message_shopping_cart(self, bots):
        shopping_list = 'Сумма к оплате:'
        for bot in bots:
            shopping_list += (
                f"\n{bot['bot__name']} {bot['price__sum']}"
            )
        return shopping_list

    def shopping_cart(self, request):
        bot = (
            Shopping_cart.objects
            .filter(bot__in_shopping_cart__user=request.user)
            .values('bot__name')
            .annotate(price__sum=Sum('price'))
            .order_by('bot__name')
        )
        return self.message_shopping_cart(bot)


class AddAndDeleteShoppingCartView(APIView):
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
