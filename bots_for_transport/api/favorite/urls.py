from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FavoriteView

app_name = 'Favorite'

router = DefaultRouter()


urlpatterns = [
    path(
        'bots/<int:id>/favorite/',
        FavoriteView.as_view(),
        name='Favorite'
    ),
    ]
