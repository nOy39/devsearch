from django.shortcuts import render

from django.http import HttpResponse
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    tags = project_obj.tag.all()
    print(tags)
    return render(request, 'projects/single-project.html', {'project': project_obj, 'tags': tags})


def createProject(request):
    context = {}
    return render(request, 'projects/project_form.html')
