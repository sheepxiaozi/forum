from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator


class Board(models.Model):
    """ 板块 """
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'tb_board'

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Comment.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Comment.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    """ 主题 """
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=True)
    starter = models.ForeignKey(User, related_name='topics', on_delete=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'tb_topic'

    def __str__(self):
        return self.subject


class Comment(models.Model):
    """ 评论 """
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=True)

    class Meta:
        db_table = 'tb_comment'

    def __str__(self):
        truncated_message = Truncator(self.message)
        # 将一个长字符串截取为任意长度字符的简便方法
        return truncated_message.chars(30)

