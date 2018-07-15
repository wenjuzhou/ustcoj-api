from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    只允许作者修改，非作者只读的权限模型。
    """

    def has_object_permission(self, request, view, obj):
        # 对任何人都允许 GET, HEAD, OPTIONS 方法
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
