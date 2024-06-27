from django.db import models


# Create your models here.
class Admins(models.Model):
    class Meta:
        db_table = "admins"

    username = models.CharField(max_length=255, null=True, verbose_name='用户名', default="")
    password = models.CharField(max_length=255, verbose_name='密码', null=True, default="")
    phone = models.CharField(verbose_name="用户手机号码", null=True, blank=True, default="", max_length=11)
    personal_info = models.TextField(verbose_name="个人简介", default="", null=True, blank=True)
    photo_url = models.TextField(verbose_name="头像地址", default="", null=True, blank=True)
    register_username = models.CharField(max_length=255, null=True, default="", blank=True, verbose_name="注册人姓名")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="数据创建时间", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="数据更新时间", null=True, blank=True)
