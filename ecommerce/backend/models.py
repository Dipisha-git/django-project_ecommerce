from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.cat_name


class Products(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(
        upload_to='productPicture', blank=True, null=True)
    price = models.IntegerField()
    description = RichTextField()

    def __str__(self):
        return self.title

    # ecommerce
    # ecommerce12345


class About(models.Model):
    bg_image = models.ImageField(
        upload_to='aboutBgPic', blank=False, null=False)
    content_img = models.ImageField(
        upload_to='contentPic', blank=True, null=True)
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=255)
    mem_image = models.ImageField(
        upload_to='memberImage', blank=True, null=True)
    position = models.CharField(max_length=255)
    details = RichTextField()

    def __str__(self):
        return self.name


class Storesetting(models.Model):
    s_name = models.CharField(max_length=255)
    s_email = models.CharField(max_length=255)
    s_phone = models.CharField(max_length=255)
    s_logo = models.ImageField(upload_to='logo', blank=True, null=True)

    def __str__(self):
        return self.s_name


class Contact(models.Model):
    fname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.fname
