from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse


from group.models import Group,GroupMember
from group.permissions import IsCreatorOrReadOnly
from group.serializers import GroupSerializer, GroupMemberSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    这个 viewset 会自动提供 `list`, `detail`, `create`, `retrieve`, `update`, `destroy` 动作.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsCreatorOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
class GroupMemberViewSet(viewsets.ModelViewSet):
    """
    这个 viewset 会自动提供 `list`, `detail`, `create`, `retrieve`, `update`, `destroy` 动作.
    """
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsCreatorOrReadOnly
    )
    def perform_create(self, serializer):
        serializer.save(group=self.request.data['groupname'],user=self.request.data['username'])

