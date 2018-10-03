from django.db import models
from tinymce import HTMLField


class Story(models.Model):
    title = models.CharField(max_length=65, unique=True)
    text = HTMLField('Content')
    pub_date = models.DateField('date published', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
