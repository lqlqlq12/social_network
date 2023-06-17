from django.contrib import admin
from employment.models import QA, QAIndex
from employment.models import Data
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class DataResource(resources.ModelResource):
    class Meta:
        model = Data
        export_order = ('date', 'url', 'content', 'voteup', 'retweet', 'comment', 'specialty', 'origin')


@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    list_display = ('date', 'url', 'content', 'voteup', 'retweet', 'comment', 'specialty', 'origin')
    search_fields = ('date', 'context', 'specialty', 'origin')
    resource_class = DataResource


class QuestionAnswerResource(resources.ModelResource):
    class Meta:
        model = QA
        export_order = ('question', 'answer')


@admin.register(QA)
class QuestionAnswerAdmin(ImportExportModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer')
    resources = QuestionAnswerResource


class QaIndexResource(resources.ModelResource):
    class Meta:
        model = QAIndex
        export_order = ('keyword', 'docList')


@admin.register(QAIndex)
class QaIndexAdmin(ImportExportModelAdmin):
    list_display = ('keyword', 'docList')
    search_fields = ('keyword',)
    resource_class = QaIndexResource
