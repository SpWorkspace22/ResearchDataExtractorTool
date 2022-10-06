import re
import authorOperations as db
from scholarly import scholarly, ProxyGenerator


def createProxyServer():
    try:
        pg = ProxyGenerator()
        success = pg.FreeProxies()
        scholarly.use_proxy(pg)
    except Exception as ex:
        print(ex)

def parseData():
    authors = db.findAuthors()

    for author in authors:
        search_query = scholarly.search_author_id(author["author_id"])
        articles = scholarly.fill(search_query)

        for publication in articles['publications']:
                papers = {}
                papers['title']=publication['bib']['title']
                papers['journal_name']=re.sub(r'[\d+\(\)\-,–…]','', publication['bib']['citation']).rstrip()
                papers['pub_year']=publication['bib']['pub_year']
                papers['number_of_citation']=publication['num_citations']
                papers['author']=author["author_id"]
                db.addPaper(papers)
        

def beginExtarction():
    #createProxyServer()
    parseData()
