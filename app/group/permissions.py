from rest_framework import permissions
from group.models import GroupMember

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    只允许管理员修改，非管理员只读的权限模型。
    """

    def has_object_permission(self, request, view, obj):
        # 对任何人都允许 GET, HEAD, OPTIONS 方法
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user
