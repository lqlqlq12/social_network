import csv
import json
import os
import re
from queue import PriorityQueue
import jieba
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger

from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger
from sklearn.feature_extraction.text import TfidfVectorizer

from employment.models import QA, QAIndex
from transformers import (
    AutoTokenizer,
    AutoModelForQuestionAnswering,
    Trainer,
    TrainingArguments,
    squad_convert_examples_to_features, pipeline
)

# 训练模型,启动项目后就会训练模型
try:

    stopwords = []
    static_path = os.path.join(settings.STATIC_ROOT, 'refs')
    file_path = os.path.join(static_path, 'stopwords.txt')
    for word in open(file_path, encoding='utf-8'):
        stopwords.append(word)

    qlist = []
    alist = []
    data = QA.objects.all()
    for item in data:
        qlist.append(item.question)
        alist.append(item.answer)
    qlist_seg = []
    for word in qlist:
        word_list = []
        text = re.sub(r'[^\w]+', '', word.strip())
        cut_text = jieba.lcut(text, cut_all=False)
        for cut in cut_text:
            if cut not in stopwords:
                word_list.append(cut)
        qlist_seg.append(word_list)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([' '.join(word_list) for word_list in qlist_seg])
except Exception:
    print('训练失败')


# Create your views here.
def homePage(request):
    return render(request, "homePage.html")


# 定义回答页面
def questionAnswer(request):
    question = request.GET['text']
    q_word_list = []
    q_text = re.sub(r'[^\w]+', '', question.strip())
    q_cut_text = jieba.lcut(q_text, cut_all=False)
    for cut in q_cut_text:
        if cut not in stopwords:
            q_word_list.append(cut)
    q_vector = vectorizer.transform([' '.join(q_word_list)])
    sim = (X * q_vector.T).toarray()
    pq = PriorityQueue()
    for cur in range(sim.shape[0]):
        pq.put((sim[cur][0], cur))
        if len(pq.queue) > 5:
            pq.get()
    pq_rank = sorted(pq.queue, key=lambda x: x[0], reverse=True)
    # print([item[0] for item in pq_rank][0])
    answer = [alist[item[1]] for item in pq_rank][0]
    print(answer)
    return render(request, 'questionAnswer.html')


# 定义分类页面
def classification(request):
    return render(request, 'classification.html')


def sentiment(request):
    return render(request, 'sentiment.html')


# 将csv数据写入数据库
def writeToDB(request):
    file_path = 'D:\\courses\\juniorsec\\social_network\\lab\\final\\code\\Policy\\qa.csv'
    with open(file_path, 'r', encoding='utf_8_sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            obj = QA(question=row['question'], answer=row['answer'])
            obj.save()


# 建立索引
def buildIndex(request):
    # 初始化停用词表
    stopwords = []
    static_filepath = os.path.join(settings.STATIC_ROOT, 'refs')
    file_path = os.path.join(static_filepath, 'stopwords.txt')
    for word in open(file_path, encoding='utf-8'):
        stopwords.append(word)
    qa_list = QA.objects.values('id', 'question', 'answer')
    all_keywords = []  # 统计全部问题和答案的关键字
    qa_dict = {}  # 统计每一对问答的关键字，key是id，value是关键字
    for qa in qa_list:
        qa_id = qa['id']
        text = qa['question'] + qa['answer']
        # 正则表达式去除非文字和数字的字符
        qa_text = re.sub(r'[^\w]+', '', text.strip())
        cut_text = jieba.cut(qa_text, cut_all=False)
        keywordList = set()
        for word in cut_text:
            if word not in stopwords:
                keywordList.add(word)
        all_keywords.extend(keywordList)
        qa_dict[qa_id] = keywordList
    count_all_keywords = set(all_keywords)
    for term in count_all_keywords:
        temp = []  # 用来存放包含这个关键字的问答对的id
        for m_id in qa_dict.keys():
            cut_text = qa_dict[m_id]
            if term in cut_text:
                temp.append(m_id)
        # 存储索引到数据库
        try:
            exist_list = QAIndex.objects.get(keyword=term)
            exist_list.docList = json.dumps(temp)
            exist_list.save()
        except ObjectDoesNotExist:
            new_list = QAIndex(keyword=term, docList=json.dumps(temp))
            new_list.save()
