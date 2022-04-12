from ast import Return
from multiprocessing import context
from pickletools import read_unicodestring1
import re
from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
# Create your views here.


def job_list(request):
    # model Query set
    # https://docs.djangoproject.com/en/4.0/ref/models/querysets/
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 1)  # Show 1 job per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    context = {'job': job_detail}
    return render(request, 'job/job_detail.html', context)

