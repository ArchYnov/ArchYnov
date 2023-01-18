from fastapi import FastAPI

from .router import Router
from .config import Settings
from .config import DatabaseNoSQL

class App():
    def __init__(self, title, settings: Settings):
        self.settings = settings
        self.router = Router(self.settings)
        self.db = DatabaseNoSQL(self.settings)
        self.app = FastAPI(title=title, dependencies=[])

    def create_router(self):
        for router in self.router():
            self.app.include_router(router, prefix=self.settings.API_V1_STR, tags=["api_v1"])
        # self.app.include_router(self.router, prefix=self.settings.API_V1_STR, tags=["api_v1"])
        # self.app.add_api_route(self.settings.API_V1_STR, self.router)
        print(self.app.routes)
        
    def create_database(self):
        self.db.create_database()

    def __call__(self):
        return self.app