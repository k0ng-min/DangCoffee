from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='아이디')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="회원가입 시점")

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Registered_User'
