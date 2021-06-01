from django.shortcuts import render
# importing loading from django template
from django.template import loader
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def whatsapp(request):
    template = loader.get_template('whatsapp.html')
    return HttpResponse(template.render())