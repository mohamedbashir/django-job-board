from pydoc import describe
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

'''
Django model field :

    - html Widget
    - Validation
    - db size

كل مره بتعدل علي ملف الموديل لازم تكتب امرين :

python manag.py makemigrations
ودي الديجانو بتشوف اذا ينفع الفيلد يتحول لكويري في الداتا بيز فبيتاكد اذا ينفع ولا لا يتعمل في الداتا بيز , لو مطلعش ايرور ده معناه انه ينفع يتنفذ علي الداتا بيز , علشان انفذه اكتب 

python manage.py migrate 

'''

JOB_TYPE = (
    ('Full Type', 'Full Type'),
    ('Part Type', 'Part Type')
)


class Job(models.Model):  # Table
    title = models.CharField(max_length=100)  # Column
    # Location

    job_type = models.CharField(max_length=15, choices=JOB_TYPE)

    description = models.TextField(max_length=1000)

    published_at = models.DateTimeField(auto_now=True)

    vacancy = models.IntegerField(default=1)

    salary = models.IntegerField(default=0)

    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title