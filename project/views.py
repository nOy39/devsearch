from django.shortcuts import render

from django.http import HttpResponse
from .models import Project
project_list = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce site'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where i built out my portfolio'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am still working on'
    }
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    tags = project_obj.tag.all()
    print(tags)
    return render(request, 'projects/single-project.html', {'project': project_obj, 'tags': tags})
