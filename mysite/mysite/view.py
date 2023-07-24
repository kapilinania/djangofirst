from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse("welcome to nsti jodhpur")


def course(request):
    return HttpResponse("<b>welcome to this course</b>")


def coursenext(request,courseid):
    return HttpResponse("welcome to this next course</b>" + courseid)

def homePage(request):
    data = {
        'title' : 'kapil',
        'body' : 'welcome to kapil',
        'clist'  : ['php', 'java','c']
    }
    return  render(request, "index.html",data)