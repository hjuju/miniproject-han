from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField()
    # author: 추후 작성 예정

    class Meta:
        managed = True
        db_table = 'posts'