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

def findAuthors():
    try:
        authors = authorCollection.find({})
        return authors
    except Exception as ex:
        print(ex)

def removeAuthorById(author_id):
    try:
        authorCollection.delete_one({"author_id":author_id})
        print("Author Removed")
    except Exception as ex:
        print(ex)

def addPaper(paper):
    try:
        paperCollection.insert_one(paper)
        print("Paper Added")
    except Exception as ex:
        print(ex)

def findPaperByAuthorId(author_id):
    pass

def findAllPapers():
    pass

def updatePaper():
    pass

def removePaper():
    pass

