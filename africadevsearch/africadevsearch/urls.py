from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def projects(requests):
    return HttpResponse('Here is the page')

def project(request, pk):
    return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name= "projects"),
    path('project/<str:pk>/', project, name="project"),
]
