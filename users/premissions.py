from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='Модераторы').exists()

    def has_object_permission(self, request, view, obj):
        # Модераторы могут видеть и редактировать любые объекты
        return request.user.is_authenticated and request.user.groups.filter(name='Модераторы').exists()


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user