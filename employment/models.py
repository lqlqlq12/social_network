from django.db import models
from django.contrib import admin


# Create your models here.
class Test(models.Model):
    data_question = models.TextField()
    data_context = models.TextField()

    def __str__(self):
        return self.data_question


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