from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Task(BaseModel):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress ", "In Progress"),
            ("Completed", "Completed"),
        ], default="pending"
    )

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Note(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)

    def __str__(self):
        return self.content

class SubTask(BaseModel):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress ", "In Progress"),
            ("Completed", "Completed"),
        ], default="pending"
    )
    class Meta:
            verbose_name = "SubTask"
            verbose_name_plural = "SubTasks"
            ordering = ['title']
    
    def __str__(self):
        return self.title