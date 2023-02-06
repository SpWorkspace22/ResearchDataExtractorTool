from django.shortcuts import HttpResponseRedirect, redirect, render
from django.http import HttpResponse
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework.response import Response

from .scanner import authorOperations as author
from .scanner import paperExtract as scanner

departments = ["MCA","M.TECH","B.TECH"]

# Create your views here.
def getIndexView(request):
    author_count = author.getAuthorCount()
    papers_count = author.getPapersCount()
    max_cit = author.getMaxCitation()
    summary = {
        "authors":author_count,
        "papers":papers_count,
        "max_cit":max_cit
        }
    return render(request,"index.html",summary)

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
    papers = {}
    filter_criteria = {}
    if request.method=='POST':
        if(request.POST['author']!=''):
            filter_criteria['author']=request.POST['author']
        
        if(request.POST['pub_year']!=''):
            filter_criteria['pub_year']=int(request.POST['pub_year'])
            print(filter_criteria)

        papers = author.findPapers(filter_criteria)

    else:
        papers = author.findPapers(filter_criteria)
    return render(request, 'papers.html', {"all_papers":papers})


# Scanner Related

def getAuthorData(request):
    scanner.beginExtarction()
    return HttpResponseRedirect(reverse('index',kwargs=()))


# Author to Paper Navigartion

def getAuthorById(request,author_id):

    filter_criteria = {'author':author_id}
    
    papers = author.findPapers(filter_criteria)
    return render(request, 'papers.html', {"all_papers":papers})


# ChartDemo

class CharData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request,format=None):
        data = {}
        data['yearSummary'] = author.getPaperCountByYear()
        data['authorSummary'] = author.getPaperCountByAuthor()
        return Response(data)