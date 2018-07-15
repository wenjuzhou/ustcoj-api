from rest_framework import viewsets
from django.contrib.auth.models import User

from user.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    这个 viewset 会自动提供 `list` 和 `detail` 动作.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
