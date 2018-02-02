from django.contrib import admin
from blog.models import Post, Tag, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)

# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-options