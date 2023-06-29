from django.shortcuts import render
from . import models
# Create your views here.


def home(request):
    project = models.Project.objects.all()

    return render(request,'home.html', {
        'project':project
    })