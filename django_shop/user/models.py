from django.db import models

# Create your models here.

class user(models.Model):
    email = models.EmailField(verbose_name="이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    register = models.DateTimeField(auto_now_add=True, verbose_name="가입일")
    
    class Meta:
        db_table = 'shoppingmall_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'