from django.contrib import admin

# Register your models here.
from .models import Task, Priority, Note, SubTask, Category

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name")
    search_fields = ("name")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name")
    search_fields = ("name")

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "priority", "category")
    search_fields = ("title", "description")
    list_filter = ("status", "priority", "category")

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "status")
    search_fields = ("title")
    list_filter = ("title", "status")

admin.site.register(Note)