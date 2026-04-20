from django.contrib import admin
from .models import Category, Project

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'tech_stack')
    list_filter = ('category',)
    search_fields = ('title', 'tech_stack')
