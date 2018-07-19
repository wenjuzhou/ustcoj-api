from django.contrib import admin
from group.models import Group, GroupMember


class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMember, GroupAdmin)