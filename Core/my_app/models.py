from django.db import models
from django.urls import reverse
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("my_app:detail",kwargs={'pk':self.pk})
