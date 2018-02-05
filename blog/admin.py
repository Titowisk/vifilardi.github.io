from django.contrib import admin
from blog.models import Post, Tag, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    exclude = ('slug', 'posted')
    list_display = ('title', 'slug', 'category', 'updated', 'posted')
    filter_vertical = ('tag',)

    empty_value_display = 'Waiting posting'

class TagAdmin(admin.ModelAdmin):
    
    exclude = ('slug',)
    list_display = ('title', 'slug', 'updated', 'created')

class CategoryAdmin(admin.ModelAdmin):
    
    fields = ('title', 'description')
    list_display = ('title', 'slug', 'updated', 'created')

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)

# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-options