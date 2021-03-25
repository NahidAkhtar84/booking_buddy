import os
import random
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from django.db import models
from PIL import Image

import string
from django.utils.text import slugify


# generate slug
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


# Create your models here.

def image_path(instance, filename):
    base_name, f_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''.join((random.choice(chars)) for _ in range(20))
    return 'blog/blog_img_{randomstring}{ext}'.format(basename=base_name, randomstring=random_str, ext=f_extension)

class Comment(models.Model):
    blog = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=400)
    phone = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.blog.title, self.name)


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    details = RichTextField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    images = models.ImageField(blank=True, null=True, upload_to=image_path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.images.path)
        img.save(self.images.path, quality=20, optimize=True)

    def __str__(self):
        return f'{self.title}'


def slug_gen(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_gen, sender=BlogPost)
