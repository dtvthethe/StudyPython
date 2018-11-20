from django.db import models

# Create your models here.
from django.utils.html import format_html


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title


    def __str__(self):
        return self.title

    def timestamp_red_color(self):
        return format_html('<span style="color: red">{}</span>', self.timestamp)
