from django.db import models

from .helpers import *

# Create your models here.
class Fonts(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    metakeyword = models.CharField(max_length=200, null=True)
    header_image = models.ImageField(upload_to='header_image')
    upload_fonts = models.FileField(upload_to="upload_fonts")
    short_dis = models.TextField()
    long_dis = models.TextField()
    char_maping = models.ImageField(upload_to='char_maping')
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self , *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Fonts, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}'





