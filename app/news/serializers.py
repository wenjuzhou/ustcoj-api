from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = News
        fields = ('id', 'title', 'author', 'summary', 'content', 'created')


