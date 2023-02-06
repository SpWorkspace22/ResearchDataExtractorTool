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
        cur = findPapers(filter_criteria)
        found = list(cur)
        if(len(found)==0):
            paperCollection.insert_one(paper)
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



# Summary Functions
def getAuthorCount():
    authors_count = 0
    
    try:
        authors_count = authorCollection.find({}).count()
    except Exception as ex:
        print(ex)

    return authors_count

def getPapersCount():
    paper_count = 0
    
    try:
        paper_count = paperCollection.find({}).count()
    except Exception as ex:
        print(ex)

    return paper_count

def getMaxCitation():
    max_cit = 0
    try:
        a = paperCollection.find({}).sort([("number_of_citation",-1)]).limit(1)
        for i in a:
            max_cit = i["number_of_citation"]
    except Exception as ex:
        print(ex)
    return max_cit



# Aggregation Operations

def getPaperCountByYear():
    # db.papers.aggregate([{$group:{_id:"$pub_year",total_paper:{$sum:1}}}])

    agg_result = paperCollection.aggregate([
        {"$group":{"_id":"$pub_year","total_paper":{"$sum":1}}},
        {"$sort":{"_id":1}}
        ])
    yearSummary = {'labels':[],'paperCount':[],'chartLabel':'Year Wise Published Paper'}
    
    for summary in agg_result:
        yearSummary['labels'].append(summary['_id'])
        yearSummary['paperCount'].append(summary['total_paper'])
    
    return yearSummary

def getPaperCountByAuthor():

    agg_result = paperCollection.aggregate([
        {"$group":{"_id":"$author","total_paper":{"$sum":1}}},
        {"$sort":{"_id":1}}
        ])

    authorSummary = {'labels':[],'paperCount':[],'chartLabel':'Paper Publish By Authors'}
    
    for summary in agg_result:
        authorSummary['labels'].append(
            findAuthorById({'author_id':summary['_id']})['author_name'])
        authorSummary['paperCount'].append(summary['total_paper'])
    
    return authorSummary
    
    

