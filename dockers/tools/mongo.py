from pymongo import MongoClient

# A Completer
class MongodbClient():

    def __init__(self):
        self.client = MongoClient("mongodb://root:root@mongo:27017/")
        self.db = self.client["ydays"]

    def getCollection(self, name_collection):
        """get collection

        Args:
            name_collection (str): name of the collection

        Returns:
            collection: collection
        """

        collection = self.db[name_collection]
        collection = self.db.get_collection(name_collection)
        return collection
    
    def getAllDocumentsFromCollection(self, name_collection, column= {}):
        """get all documents

        Args:
            name_collection (str): name of the collection

        Returns:
            collection: collection
        """
        
        collection = self.db[name_collection]
        allCollection = collection.find({}, column)
        return allCollection
    

    def insertOne(self, name_collection, data,  checkDuplicates = []):
        """insert un element en base de données

        Args:
            name_collection (str)   : Name of the collection
            data (dict)             : data insert in bdd
            checkDuplicates (list)  : columns check duplicates
        """
        collection = self.getCollection(name_collection)

        # on creer notre critére pour recuperer les duplicates
        findCriteria = {"$or": []}
        for column in checkDuplicates:
            findCriteria["$or"].append({column : data[column]})

        data_duplicate = collection.find_one(findCriteria)
        # Si la données n'existe pas dans la collection on insere
        if not data_duplicate:
            collection.insert_one(data)  
    

    def insertMany(self, name_collection, data, checkDuplicates = []) :
        """insert plusieurs elements en base de données

        Args:
            name_collection (str)   : Name of the collection
            data (list)             : data insert in bdd
            checkDuplicates (list)  : columns check duplicates
        """
        collection = self.getCollection(name_collection)
        findCriteria = {"$or" : []}
        for column in checkDuplicates:
            findCriteria["$or"].append({column : { "$in" : [ele[column] for ele in data]}})
        
        duplicates = {}
        for column in checkDuplicates :
            duplicates[column] = [ele[column] for ele in collection.find(findCriteria)]

        dataToInsert = []
        for column in checkDuplicates:
            for element in data:
                if element[column] not in duplicates[column] and element not in dataToInsert:
                    dataToInsert.append(element)
        
        if dataToInsert :
            collection.insert_many(dataToInsert) 

    def get_documents(self, collection:object, criterion:dict = {}):
        """get documents from collection

        Args:
            collection (str)    : name of collection
            criterion (dict)    : criterion for mongo find

        Returns:
            documents: mongo query return
        """
        return [[document['_id'], document['_source']['text']] for document in self.db[collection].find(criterion)]
    
    def update_one(self, collection:str, query:dict, values:dict):
        """update documents from collection

        Args:
            collection (str)    : name of collection
            query (dict)        : query to find the document to update
            values (dict)       : $set to update the value of a property

        Returns:
            documents: mongo query status return
        """
        return self.db[collection].update_one(query, values)