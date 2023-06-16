from django.contrib import admin
from employment.models import Test,Data
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

# Register your models here.
class DataResource(resources.ModelResource):

    class Meta:
        model = Data
        export_order = ('date','url','context','voteup','retweet','comment','specialty','origin')

@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    list_display = ('date','url','context','voteup','retweet','comment','specialty','origin')
    search_fields = ('date','context','specialty','origin') 
    resource_class = DataResource