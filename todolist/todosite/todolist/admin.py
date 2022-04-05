from django.contrib import admin
from .models import *
# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_finished', 'serious_category')
    list_display_links = ('id','title')
    list_editable = ('is_finished',)
    search_fields = ('id','title','content')
    list_filter = ('is_finished','serious_category')
    
admin.site.register(Tasks, TasksAdmin)
admin.site.register(SeriousCategory)