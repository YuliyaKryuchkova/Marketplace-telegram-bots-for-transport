from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .bot.views import BotViewSet
from .categories.views import CategoryViewSet
from .favorite.views import FavoriteView, FavoriteListView
from .rating.views import RatingCreateView
from .reviews.views import ReviewCreateView
from .shopping_cart.views import AddAndDeleteShoppingCartView, \
    ShoppingCartRetrieveView
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
        AddAndDeleteShoppingCartView.as_view(),
        name='Shopping_cart'
    ),
    path(
        'users/<int:pk>/shopping_cart/',
        ShoppingCartRetrieveView.as_view(),
        name='Shopping_cart'
    ),
    path(
        'bots/<int:pk>/review/',
        ReviewCreateView.as_view(),
        name='review'
    ),
    path(
        'bots/<int:id>/favorite/',
        FavoriteView.as_view(),
        name='Favorite'
    ),
    path(
        'users/<int:id>/favorite/',
        FavoriteListView.as_view(),
        name='Favorite'
    ),
    path(
        'users/reset-password/',
         CustomPasswordResetView.as_view(),
         name='password_reset'
    ),
    path(
        'bots/<int:pk>/rating/',
        RatingCreateView.as_view(),
        name='rating'
    ),
]
