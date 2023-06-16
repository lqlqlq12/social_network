from django.contrib import admin
from employment.models import Test, QA, QAIndex
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class TestResource(resources.ModelResource):

    class Meta:
        model = Test
        export_order = ('data_question','data_context')

@admin.register(Test)
class TestAdmin(ImportExportModelAdmin):
    list_display = ('data_question','data_context')
    search_fields = ('data_question',)  
    resource_class = TestResource



class QuestionAnswerResource(resources.ModelResource):
    class Meta:
        model = QA
        export_order = ('question', 'answer')


@admin.register(QA)
class QuestionAnswerAdmin(ImportExportModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question','answer')
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