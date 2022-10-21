from django.shortcuts import HttpResponseRedirect, render
from django.http import HttpResponse
from django.urls import reverse

from .scanner import authorOperations as author


# Create your views here.

def getIndexView(request):
    return render(request,"index.html",{})

def getAuthors(request):
    authors = author.findAuthors()
    return render(request,"authors.html",{"all_authors":authors})

def getAuthorsById(request, author_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def removeAuthor(request, author_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def createNewAuthor(request):
    return render(request, 'new_author.html', {})

def addNewAuthor(request):
    newAuthor = {}
    newAuthor['author_id']=request.POST['author_id']
    newAuthor['author_name']=request.POST['author_name']
    newAuthor['affiliation']=request.POST['affiliation']
    
    print(author.addAuthor(newAuthor))

    return HttpResponseRedirect(reverse('new_authors', args=()))