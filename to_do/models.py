from django.db import models

# Create your models here.
class ToDo(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=240)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content
