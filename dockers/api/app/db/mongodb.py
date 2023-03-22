from typing import Any
from pymongo import MongoClient
from fastapi import FastAPI

from settings.config import Settings

class Mongo:
    def __init__(self, config: Settings):
        self.config = config
        self.client = MongoClient(self.config.MONGO_URL)
        self.db = None

    async def connect(self):
        # self.client = MongoClient(self.config.MONGO_URL)
        self.db = self.client[self.config.MONGO_DB_NAME]

    async def close(self):
        self.client.close()
    
    def session(self):
        return self.client.start_session()
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
