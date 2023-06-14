from django.urls import re_path as url
from employment import views

urlpatterns = [
    url(r'^$',views.homePage,name='homePage'),
    url(r'^classification', views.classification, name='classification'),
    url(r'^questionAnswer', views.questionAnswer, name='questionAnswer'),
    url(r'^sentiment', views.sentiment, name='sentiment'),
]