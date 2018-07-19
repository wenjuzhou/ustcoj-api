from rest_framework import serializers

from group.models import Group,GroupMember


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    member = serializers.ReadOnlyField(source='member.username')
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'created', 'creator', 'member')

class GroupMemberSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    group = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = GroupMember
        fields = ('id', 'user', 'group', 'auth_grade')

