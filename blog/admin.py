from django.contrib import admin
from . models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
       list_display = ('title', 'slug', 'author', 'publish', 'status')
       list_filter = ('author','status', 'created', 'publish')
       search_fields = ('title', 'body')
       prepopulated_fields = {'slug': ('title',)}
       raw_id_fields = ('author',)
       date_hierarchy = 'publish'
       ordering = ('status', 'publish')

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#        #data_hierarchy = 'publish'
#        pass
