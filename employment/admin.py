from django.contrib import admin
from employment.models import Data
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class DataResource(resources.ModelResource):

    class Meta:
        model = Data
        export_order = ('date','url','content','voteup','retweet','comment','specialty','origin')

@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    list_display = ('date','url','content','voteup','retweet','comment','specialty','origin')
    search_fields = ('date','context','specialty','origin') 
    resource_class = DataResource