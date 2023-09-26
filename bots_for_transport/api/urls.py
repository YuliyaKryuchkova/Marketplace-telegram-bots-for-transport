from django.contrib.auth import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .bot.views import BotViewSet
from .categories.views import CategoryViewSet
from .favorite.views import FavoriteView
from .rating.views import RatingViewSet
from .shopping_cart.views import Shopping_cartView
from .users.views import CustomDjoserUserViewSet

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register(
    'bots',
    BotViewSet,
    basename='bots')

router_v1.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)
router_v1.register(
    r'bots/(?P<bot_id>[^/.]+)/ratings',
    RatingViewSet,
    basename='ratings'
)
router_v1.register(
    'users',
    CustomDjoserUserViewSet,
    basename='users'
)
router_v1.register(
    'bots',
    BotViewSet,
    basename='bots')


urlpatterns = [
    path(
        '',
        include(router_v1.urls)
    ),
    path(
        'auth/',
        include('djoser.urls.authtoken')
    ),
    path(
        'bots/<int:id>/shopping_cart/',
        Shopping_cartView.as_view(),
        name='Shopping_cart'
    ),
    path(
        'bots/<int:id>/favorite/',
        FavoriteView.as_view(),
        name='Favorite'
    ),
]
