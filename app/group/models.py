from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(
        'auth.user', related_name='creator', on_delete=models.CASCADE)
    member = models.ManyToManyField(
        'auth.user', through='GroupMember', through_fields=('group', 'user'), related_name='member')

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Group, self).save(*args, **kwargs)
class GroupMember(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    user = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    auth_grade = models.IntegerField(default=0)

    class Meta:
        unique_together = ('group', 'user')

    def save(self, *args, **kwargs):
        super(GroupMember, self).save(*args, **kwargs)
