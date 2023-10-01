from django.contrib import admin
from django.urls import include, path
from yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/bots-auth/', include('rest_framework.urls')),
]

urlpatterns += doc_urls
