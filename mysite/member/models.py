from django.db import models

# Create your models here.

class Member(models.Model):
    user_id = models.CharField(max_length=256, verbose_name='아이디')
    password = models.CharField(max_length=256, verbose_name='비밀번호')
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='가입일자')

    def __str__(self):
        return self.user_id
