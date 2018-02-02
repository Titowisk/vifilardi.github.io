from django.contrib import admin
from blog.models import Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    fields = ('title', 'text', 'language', 'tag')
    list_display = ('title', 'slug', 'posted', 'created')
    date_hierarchy = 'created'
    empty_value_display = 'not published yet'

class TagAdmin(admin.ModelAdmin):
    
    fields = ('tag',)
    list_display = ('tag', 'slug', 'created', 'modified')

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)

# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-options