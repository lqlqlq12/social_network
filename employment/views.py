from django.shortcuts import render
from django.core.paginator import Paginator,Page,EmptyPage,PageNotAnInteger
from employment.models import Test

# Create your views here.
def homePage(request):
    data_list = Test.objects.all()
    paginator = Paginator(data_list,20)
    page = request.GET.get('page')
    list = []
    if page:
        list = paginator.page(page).object_list
    else:
        list = paginator.page(1).object_list
    try:
        page_object = paginator.page(page)
    except PageNotAnInteger:
        page_object = paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)
    return render(request, "homePage.html", {
	    'page_object':page_object,
	    'data_list':list
	})

# 定义回答页面
def questionAnswer(request):
    return render(request,'questionAnswer.html')

# 定义分类页面
def classification(request):
    return render(request,'classification.html')

def sentiment(request):
    return render(request,'sentiment.html')