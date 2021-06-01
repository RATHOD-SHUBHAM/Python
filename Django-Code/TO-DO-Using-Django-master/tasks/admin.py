from django.contrib import admin

# Register your models here.


from .models import *

# step 13 :
admin.site.register(Task)
