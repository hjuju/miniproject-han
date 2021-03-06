from django.db import models


class BoardVO(models.Model):
    # id = models.AutoField(primary_key=True) 생략해야 자동 생성됨
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)  # 자동으로 db에 찍힘
    updated_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정

    class Meta:
        managed = True
        db_table = 'posts'

    def __str__(self):
        return f'[{self.pk}] is username = {self.sequence},' \
               f'title = {self.title}' \
               f'content = {self.content}' \
               f'created_at = {self.created_at}' \
               f'updated_at = {self.updated_at}'
