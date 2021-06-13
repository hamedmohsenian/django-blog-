from django.shortcuts import render
from django.shortcuts import HttpResponse

#main page

def Home(request):
    #return HttpResponse ("this is main page")
    return render(request, "home.html")

#about

def about(request):
    #return HttpResponse ("this is about page")
    return render(request, "about.html")


#first
def first(request):
    #return HttpResponse ("this is first page")
    return render(request, "first.html")
