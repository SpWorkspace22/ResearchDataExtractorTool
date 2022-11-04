import pymongo
import utils as client;

db = client.getConnection()
authorCollection =  db.authors
paperCollection = db.papers

# author crud
def addAuthor(author):
    try:
        found = findAuthorById({"author_id":author["author_id"]})
        if found==None:
            authorCollection.insert_one(author)
            print("Author Added")
        else:
            updateAuthor(author)
    except Exception as ex:
        print(ex)


def updateAuthor(author):
    try:
        filter_criteria = {"author_id":author["author_id"]}
        authorCollection.update_one(filter_criteria,{"$set":author})

        print("Author Updated")
    except Exception as ex:
        print(ex)
    

def findAuthorById(filter_criteria):
    author = authorCollection.find_one(filter_criteria)
    if(author==None):
        return None
    else:
        return author

def findAuthors(filter_criteria):
    try:
        authors = authorCollection.find(filter_criteria)
        return authors
    except Exception as ex:
        print(ex)

def removeAuthorById(author_id):
    try:
        authorCollection.delete_one({"author_id":author_id})
        print("Author Removed")
    except Exception as ex:
        print(ex)

# Paper Crud
def addPaper(paper):
    try:
        filter_criteria = {'author':paper['author'],'title':paper['title']}
        found = findPapers(filter_criteria)
        if(found==None):
            paperCollection.insert_one(paper)
            print("Paper Added")
        else:
            updatePaper(filter_criteria,paper)
    except Exception as ex:
        print(ex)

def findPapers(filter):
    try:
        papers = paperCollection.find(filter).sort('pub_year',-1)
        print(papers)
        return papers
    except Exception as ex:
        print(ex)

def updatePaper(filter_criteria,paper):
    try:
        authorCollection.update_one(filter_criteria,{"$set":paper})
        print("Paper Updated")
    except Exception as ex:
        print(ex)

def removePaper():
    pass

