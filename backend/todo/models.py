from django.db import models

# Create your models here.


    # these are properties of Todo model
class Todo(models.Model):
      title = models.CharField(max_length=120)
      description = models.TextField()
      completed = models.BooleanField(default=False)

      def _str_(self):
        return self.title