from django.db import models
from django.contrib import admin

class Data(models.Model):
    date = models.TextField()       # 时间
    url = models.TextField()        # 网站
    content = models.TextField()    # 内容
    voteup = models.TextField()     # 点赞
    retweet = models.TextField()    # 转发
    comment = models.TextField()    # 评论
    specialty = models.TextField()  # 专业
    origin = models.TextField()     # 来源
    def __str__(self):
        return self.content