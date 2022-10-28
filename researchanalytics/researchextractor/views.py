from tkinter.messagebox import RETRY
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.http import HttpResponse
from django.urls import reverse

from .scanner import authorOperations as author

departments = ["MCA","M.TECH","B.TECH"]

# Create your views here.

def getIndexView(request):
    return render(request,"index.html",{})

def createNewAuthor(request):
    return render(request, 'new_author.html', {"departments":departments})

def addNewAuthor(request):
    newAuthor = {}
    newAuthor['author_id']=request.POST['authorId']
    newAuthor['author_name']=request.POST['authorName']
    newAuthor['affiliation']=request.POST['affiliate']
    newAuthor['department']=request.POST['depart']
    newAuthor['email']=request.POST['email']
    newAuthor['phone']=request.POST['phone']
    
    if(newAuthor['department'] not in departments):
        return render(request, 'new_author.html', 
            {"departments":departments,"error":"Please Select Correct Department"})
    
    if author.findAuthorById({"author_id":newAuthor['author_id']}):
        author.updateAuthor(newAuthor)
    else:
        author.addAuthor(newAuthor)

    return render(request, 'new_author.html', 
            {"departments":departments,"success":"Author Changes Saved"})

def editAuthor(request,author_id):
    edit_author = author.findAuthorById({"author_id":author_id})
    return render(request, 'new_author.html', 
    {"author":edit_author,"edit":"readonly","departments":departments})

def removeAuthor(request, author_id):
    author.removeAuthorById(author_id)
    return HttpResponseRedirect(reverse('authors', kwargs={}))

def getAuthors(request):
    authors = author.findAuthors({})
    return render(request,"authors.html",{"all_authors":authors})

def getAuthorsById(request):
    filter = {"author_id":request.POST['authorId']}
    if(filter['author_id']==""):
        filter = {}
    authors = author.findAuthors(filter)
    return render(request,"authors.html",{"all_authors":authors})


def getPapers(request):
    papers = author.findPapers({})
    return render(request, 'papers.html', {"all_papers":papers})