from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView
from djoser.views import UserViewSet

User = get_user_model()


class CustomDjoserUserViewSet(UserViewSet):
    pagination_class = None


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration / password_reset_form.html '
