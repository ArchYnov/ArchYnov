from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.routes.movies import router as movies_router
from app.routes.news import router as news_router
from mongodb import Mongo
from config import Settings


settings = Settings()
app = FastAPI()
mongo = Mongo(settings)

app.config = settings
app.mongodb_client = mongo

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]
)
app.add_middleware(
    HTTPSRedirectMiddleware
)


@app.on_event("startup")
async def startup():
    await app.mongodb_client.connect()
    print("Connected to the MongoDB database!", mongo.client)


@app.on_event("shutdown")
async def shutdown():
    await app.mongodb_client.close()
    print("Disconnected from the MongoDB database!")

app.include_router(movies_router, prefix=app.config.API_PREFIX, tags=["v1"])
app.include_router(news_router, prefix=app.config.API_PREFIX, tags=["v1"])
