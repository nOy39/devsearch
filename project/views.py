from django.shortcuts import render

from django.http import HttpResponse

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
    page = "projects"
    num = 15
    context = {'page': page, 'num': num, 'projects': project_list}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = None
    for i in project_list:
        if i['id'] == pk:
            project_obj = i
    return render(request, 'projects/single-project.html', {'project': project_obj})
