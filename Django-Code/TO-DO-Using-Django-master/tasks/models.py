# step 11 :
from django.db import models

# Create your models here.
class Task(models.Model):
    # Form fields
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add=True)  # date it was created



    # It is actually a general python method.
    # It is called automatically when you either use “print” or “str” to convert your object to string.
    # It is predifined for every class.
    # But if you want to customise the output you want to give for your class you can use it.
    def __str__(self):
        return self.title