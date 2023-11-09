from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Проверяет, является ли пользователь автором объекта или разрешено ли
    только чтение."""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated and request.user.is_author)


class IsAuthor(permissions.BasePermission):
    """Проверяет, является ли пользователь автором объекта."""
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user and request.user.is_author)


class IsOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь владельцем объекта."""
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
