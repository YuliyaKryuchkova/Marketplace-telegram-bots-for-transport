from pathlib import Path
import os

from environs import Env

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ftwj&rd_2*a76-j+r^_3$%p456#=8^y(=fh0zmurni0jce$tl-'

DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = ['ALLOWED_HOSTS', '*']

CORS_ORIGIN_ALLOW_ALL = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'django_filters',
    'drf_yasg',
    'api.apps.ApiConfig',
    'users.apps.UsersConfig',
    'bot.apps.BotConfig',
    'rating.apps.RatingConfig',
    'reviews.apps.ReviewsConfig',
    'categories.apps.CategoriesConfig',
    'shopping_cart.apps.Shopping_cartConfig',
    'favorite.apps.FavoriteConfig',
    'django_extensions',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bots_for_transport.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bots_for_transport.wsgi.application'

AUTH_USER_MODEL = 'users.User'

DEVELOPMENT = env('DEVELOPMENT', default=False) == 'True'

if DEVELOPMENT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': env('DB_ENGINE'),
            'NAME': env('POSTGRES_DB'),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
            'HOST': env('DB_HOST'),
            'PORT': env('DB_PORT')
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #         'rest_framework.authentication.BasicAuthentication',
    #         'rest_framework.authentication.SessionAuthentication',
    #     ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'CORS_ORIGIN_ALLOW_ALL': True,
}

DJOSER = {
    'PERMISSIONS': {
        'user': ['djoser.permissions.CurrentUserOrAdminOrReadOnly'],
    },
    # 'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    # 'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    # 'ACTIVATION_URL': '#/activate/{uid}/{token}',
    # 'SEND_ACTIVATION_EMAIL': True,
    # 'LOGIN_FIELD': 'email',
    'SERIALIZERS': {
        'user_create': 'api.users.serializers.CustomUserCreateSerializer',
        'user': 'api.users.serializers.CustomUserSerializer',
        'current_user': 'api.users.serializers.CustomUserSerializer',
    },

}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------------------
# почта
#  подключаем движок filebased.EmailBackend
# EMAIL_BACKEND = env("EMAIL_BACKEND")
# # указываем директорию, в которую будут складываться файлы писем

# EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')
#
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_PORT = env.int("EMAIL_PORT")
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL")
# EMAIL_DOMAIN = env("EMAIL_DOMAIN")
# SERVER_EMAIL = f"{EMAIL_HOST_USER}@{EMAIL_DOMAIN}"
# DEFAULT_FROM_EMAIL = f"{EMAIL_HOST_USER}@{EMAIL_DOMAIN}"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

PAGINATION_PAGE_SIZE = 12
