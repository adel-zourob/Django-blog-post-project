from django.contrib import admin
from .models import Category,Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass
class CategoryAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
