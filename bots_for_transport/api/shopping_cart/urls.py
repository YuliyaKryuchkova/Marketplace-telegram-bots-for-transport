from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import Shopping_cartView

app_name = 'Shopping_cart'

router = DefaultRouter()


urlpatterns = [
    path(
        'bots/<int:id>/shopping_cart/',
        Shopping_cartView.as_view(),
        name='Shopping_cart'
    ),
    ]
