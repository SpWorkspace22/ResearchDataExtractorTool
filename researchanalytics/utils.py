import pymongo 

connectionString =  "mongodb://localhost:27017"

def getConnection():
    client =""
    try:
        client = pymongo.MongoClient(connectionString)
        db = client["researchRepo"]
    except Exception as ex:
        print(ex)
    return db

