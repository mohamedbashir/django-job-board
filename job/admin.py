from django.contrib import admin

# Register your models here.

'''
وهنا بضيف الابلكيشن بتاع يوزر في الادمن 
وبعرف اعدل في شكله في الادمن

'''

from .models import Job, Category, Apply

admin.site.register(Job)

admin.site.register(Category)

admin.site.register(Apply)
