from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .categories.views import CategoryViewSet
from .users.views import CustomDjoserUserViewSet

app_name = 'api'

router_v1 = DefaultRouter()

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
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
