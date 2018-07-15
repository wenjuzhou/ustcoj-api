from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    summary = models.TextField()
    content = models.TextField()

    author = models.ForeignKey(
        'auth.user', related_name='news', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(News, self).save(*args, **kwargs)