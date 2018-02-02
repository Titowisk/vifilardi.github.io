from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'posted', 'created')
    date_hierarchy = 'created'
    empty_value_display = 'not published yet'



admin.site.register(Post, PostAdmin)