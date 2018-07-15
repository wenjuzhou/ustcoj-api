from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse


from news.models import News
from news.permissions import IsAuthorOrReadOnly
from news.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    这个 viewset 会自动提供 `list`, `detail`, `create`, `retrieve`, `update`, `destroy` 动作.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



