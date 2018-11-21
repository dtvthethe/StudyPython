from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import datetime

# Create your models here.
from django.utils.html import format_html


def upload_file_path(instance, filepath):
    # instance: current object has value
    # name.extention of file uploaded
    return '%s.%s' % (datetime.datetime.now().strftime("%d%m%Y%H%M%S%f"), filepath.split('.')[-1])


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' %(slug, qs.first().id)
        return create_slug(instance, new_slug)
    return slug


def pre_save_post_signal_receiver(sender, instance, *args, **kwargs):
    if not instance.slug: #check this becase update case
        instance.slug = create_slug(instance)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_file_path, null=True, blank=True, height_field='height_field',
                              width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def timestamp_red_color(self):
        return format_html('<span style="color: red">{}</span>', self.timestamp)

    class Meta:
        ordering = ['-timestamp', '-updated']


pre_save.connect(pre_save_post_signal_receiver, sender=Post)
