from django.db import models
from django.contrib import admin

# Create your models here.
class Test(models.Model):
    data_question = models.TextField()
    data_context = models.TextField()
    def __str__(self):
        return self.data_question