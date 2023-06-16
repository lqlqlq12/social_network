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


class QA(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return str(self.question) + str(self.answer)

#索引表
class QAIndex(models.Model):
    keyword = models.TextField()
    docList = models.TextField()

    def __str__(self):
        return self.keyword
        return self.content