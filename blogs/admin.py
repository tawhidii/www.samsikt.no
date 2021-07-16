from django.contrib import admin

from django.contrib import admin
from .models import Category, Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ('text',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
