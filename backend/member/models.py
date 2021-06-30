from django.db import models


class MemberVO(models.Model):
    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField()
    email = models.EmailField()

    # class 구조에서 메소드 없음 = value object / entity :=ValueObject 구조
    # 리액트의 sign up과 value가 같아야함

    class Meta:
        managed = True
        db_table = 'members'

        def __str__(self):
            pass





