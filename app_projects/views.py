from django.shortcuts import render

# Create your views here.
def projects(request):
    context = {}
    return render(request, "app_projects/projects.html", context)
