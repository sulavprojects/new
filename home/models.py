from turtle import title
from django.db import models
from froala_editor.fields import FroalaField
from .helpers import *

# Create your models here.
class Fonts(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    metakeyword = models.CharField(max_length=200, null=True)
    header_image = models.ImageField(upload_to='header_image')
    upload_fonts = models.FileField(upload_to="upload_fonts")
    short_dis = models.TextField()
    long_dis = FroalaField()
    char_maping = models.ImageField(upload_to='char_maping')
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self , *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Fonts, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}'


class Modification(models.Model):
    websitename = models.CharField(max_length=50)
    ouremail = models.EmailField()
    copyright = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='websiteimages')
    websitediscription = models.TextField()
    favicon = models.ImageField()

    def __str__(self):
        return self.websitename


class Pages(models.Model):
    aboutus = FroalaField()
    privacypolicy = FroalaField()
    termsandcondition = FroalaField()
    ourpages = FroalaField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return 'message from -' + self.name + ' - ' + self.email 

