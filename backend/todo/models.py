from django.db import models

# Create your models here.

class Todo(models.Model):
    # these are properties of Todo model
    title = models.CharField(max_length = 128)   # 120 in tut
    description = models.TextField()
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.title