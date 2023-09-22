from django.contrib.auth import get_user_model
from djoser.views import UserViewSet

from api.pagination import LimitPageNumberPagination

User = get_user_model()


class CustomDjoserUserViewSet(UserViewSet):
    pagination_class = LimitPageNumberPagination
