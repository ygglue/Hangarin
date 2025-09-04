from django.contrib import admin

# Register your models here.
from .models import Task, Priority, Note, SubTask, Category

admin.site.register(Task)
admin.site.register(Priority)
admin.site.register(Note)
admin.site.register(SubTask)
admin.site.register(Category)