from django.db import models

from Users.models import Users


# Create your models here.
class Works(models.Model):
    class Meta:
        db_table = 'works'
        verbose_name = '作品总表'

    work_type = models.CharField(max_length=20, verbose_name="作品类型", null=True, blank=True, default="")
    title = models.CharField(max_length=255, verbose_name="作品标题", null=True, blank=True, default="")
    worker = models.CharField(max_length=255, verbose_name="作者", null=True, blank=True, default="")
    description = models.TextField(verbose_name="作品简介", null=True, blank=True, default="")
    image_url = models.TextField(verbose_name="作品图片", null=True, blank=True, default="")
    content = models.TextField(verbose_name="正文文本", null=True, blank=True, default="")
    video_url = models.TextField(verbose_name="视频地址", null=True, blank=True, default="")
    view_count = models.IntegerField(verbose_name="观看数量", null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="数据创建时间", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="数据更新时间", null=True, blank=True)


class Likes(models.Model):
    class Meta:
        db_table = 'likes'
        verbose_name = '点赞表'

    work = models.ForeignKey(Works, on_delete=models.CASCADE, verbose_name="点赞对应的作品id")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="点赞对应人")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="数据创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="数据更新时间")


class Marks(models.Model):
    class Meta:
        db_table = 'marks'
        verbose_name = '收藏表'

    work = models.ForeignKey(Works, on_delete=models.CASCADE, verbose_name="点赞对应的作品id")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="点赞对应人")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="数据创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="数据更新时间")


class Comments(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = '评论表'

    work = models.ForeignKey(Works, on_delete=models.CASCADE, verbose_name="点赞对应的作品id")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="点赞对应人")
    content = models.TextField(verbose_name="评论内容", default="")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="数据创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="数据更新时间")


class Comments_Marks(models.Model):
    class Meta:
        db_table = 'comments_marks'
        verbose_name = '评论收藏表'

    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, verbose_name="对应的评论id")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="操作的用户")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="数据创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="数据更新时间")


class Comments_Likes(models.Model):
    class Meta:
        db_table = 'comments_likes'
        verbose_name = '评论点赞表'

    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, verbose_name="对应的评论id")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="操作的用户")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="数据创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="数据更新时间")
