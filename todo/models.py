from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    'String representation of the class'
    def __str__(self):
        return self.title