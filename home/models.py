from email.policy import default
from django.db import models
from django.forms import CharField


from .helpers import *
from froala_editor.fields import FroalaField
from taggit.managers import TaggableManager

# Create your models here.
class Fonts(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    metakeyword = models.CharField(max_length=200, null=True)
    tags = TaggableManager()
    header_image = models.ImageField(upload_to='header_image')
    headerimg_alt = models.CharField(max_length=100, default="arabic fonts")
    upload_fonts = models.FileField(upload_to="upload_fonts")
    short_dis = FroalaField()
    long_dis = FroalaField()
    char_maping = models.ImageField(upload_to='char_maping')
    charimg_alt = models.CharField(max_length=100, default="arabic fonts charecter maping image")
    publish = models.BooleanField(default=False)
    Total_downloads = models.PositiveIntegerField(default=10, blank=False, null= False)

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
    websitediscription = FroalaField()
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



