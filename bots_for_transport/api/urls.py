from django.contrib.auth import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .bot.views import BotViewSet
from .categories.views import CategoryViewSet
from .favorite.views import FavoriteView
from .shopping_cart.views import Shopping_cartView
from .users.views import CustomDjoserUserViewSet, CustomPasswordResetView

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
    'users',
    CustomDjoserUserViewSet,
    basename='users'
)

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
    path('users/reset-password/',
         CustomPasswordResetView.as_view(),
         name='password_reset'),
]
