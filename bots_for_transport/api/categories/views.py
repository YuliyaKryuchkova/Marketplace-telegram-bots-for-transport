from categories.models import Category
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import CategorySerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
