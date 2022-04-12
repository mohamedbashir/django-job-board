from distutils.command.upload import upload
from pydoc import describe
from pyexpat import model
from tkinter import image_names
from turtle import title
from unicodedata import category
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

'''
Django model field :

    - html Widget
    - Validation
    - db size

كل مره بتعدل علي ملف الموديل لازم 
تكتب امرين :

python manage.py makemigrations
ودي الديجانو بتشوف اذا ينفع الفيلد يتحول لكويري في الداتا بيز فبيتاكد اذا ينفع ولا لا يتعمل في الداتا بيز , لو مطلعش ايرور ده معناه انه ينفع يتنفذ علي الداتا بيز , علشان انفذه اكتب 

python manage.py migrate 

'''

JOB_TYPE = (
    ('Full Type', 'Full Type'),
    ('Part Type', 'Part Type')
)


def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "job/%s/%s.%s" % (instance.id, instance.id, extension)


class Job(models.Model):  # Table
    title = models.CharField(max_length=100)  # Column
    # Location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):

        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        '''
        This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object. This method must return the String object.
        '''
        return self.title


class Category(models.Model):

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name='job_apply')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cd = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)

    def __str__(self):
        return self.name
