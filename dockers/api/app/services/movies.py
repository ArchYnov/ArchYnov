from mongodb import Mongo
from app.models.movies import PyObjectId

class MovieService():
    def __init__(self, mongo: Mongo):
        self._collection = mongo.db['tmdb']

    def find(self, sort: list, limit: int, offset: int):
        return self._collection.find().sort(sort).limit(limit).skip(offset)
        
    def find_by_id(self, id: int | str): 
        try:
            query = {"_id": PyObjectId(id)}
        except:
            query = {"id": id}

        return self._collection.find_one(query)   
    
    def count(self):
        return self._collection.count_documents({})
    
    def count_by_filter(self, filter: dict):
        return self._collection.count_documents(filter)
    
    def find_by_filter(self, filter: dict, sort: list, limit: int, offset: int, project: dict = {}):
        return self._collection.find(filter, project).sort(sort).limit(limit).skip(offset)
    
    def find_by_aggregate(self, filter: list):
        return self._collection.aggregate(filter)

