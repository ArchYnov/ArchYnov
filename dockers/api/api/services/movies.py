from db.mongodb import Mongo
from api.models.movies import PyObjectId, MovieModel

class MovieService():
    def __init__(self, mongo: Mongo):
        self._collection = mongo.db['tmdb']

    def find(self, limit: int, offset: int):
        return self._collection.find().limit(limit).skip(offset)
        
    def find_by_id(self, id: int | str): 
        try:
            query = {"_id": PyObjectId(id)}
        except:
            query = {"id": id}

        return self._collection.find_one(query)   
    
    def count(self):
        return self._collection.count_documents({})