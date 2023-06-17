from django.urls import re_path as url
from employment import views

urlpatterns = [
    url(r'^$',views.homePage,name='homePage'),
    url(r'^classification', views.classification, name='classification'),
    url(r'^questionAnswer', views.questionAnswer, name='questionAnswer'),
    url(r'^sentiment', views.sentiment, name='sentiment'),
    url(r'^func', views.buildIndex), #写qa.csv到数据库,以及建立索引,想做啥就换哪个函数
]