from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'date_posted', 'date_created')
    date_hierarchy = 'date_created'
    empty_value_display = 'not published yet'



admin.site.register(Post, PostAdmin)