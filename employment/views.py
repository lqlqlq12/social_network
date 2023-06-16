from django.shortcuts import render
from django.core.paginator import Paginator,Page,EmptyPage,PageNotAnInteger


# Create your views here.
def homePage(request):
    return render(request, "homePage.html")

# 定义回答页面
def questionAnswer(request):
    return render(request,'questionAnswer.html')

# 定义分类页面
def classification(request):
    return render(request,'classification.html')

def sentiment(request):
    return render(request,'sentiment.html')