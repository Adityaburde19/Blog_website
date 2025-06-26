from django.contrib import admin
from . models import Category, Blogs

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updated_at')
    search_fields = ('category_name',)
    
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'author', 'status', 'is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'category__category_name', 'status')
    list_editable = ('status', 'is_published')
    list_filter = ('status', 'is_published', 'created_at')

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs, BlogsAdmin)

