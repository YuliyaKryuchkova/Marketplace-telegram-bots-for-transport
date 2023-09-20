from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from bot.models import Bot



class BotViewSet(ModelViewSet):
    queryset = Bot,objects.all()
