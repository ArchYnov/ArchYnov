
from fastapi import APIRouter

# from .app import App
from .config import Settings

from .routers import movie_router
from .routers import root_router


class Router:
    def __init__(self, settings: Settings):
        # self.app = app.app
        # self.router = APIRouter()
        self.router = [movie_router, root_router]
        # self.router.include_router(root_router)
        # self.router.include_router(movie_router)
        # self.app.include_router(root_router, tags=["root"])

    def __call__(self):
        return self.router


    