from fastapi import Depends, FastAPI
from api.routes.movies import router as movies_router
from db.mongodb import Mongo
from settings.config import Settings


settings = Settings()
app = FastAPI()
mongo = Mongo(settings)

app.config = settings
app.mongodb_client = mongo

@app.on_event("startup")
async def startup():
    await app.mongodb_client.connect()
    print("Connected to the MongoDB database!", mongo.client)

@app.on_event("shutdown")
async def shutdown():
    await app.mongodb_client.close()
    print("Disconnected from the MongoDB database!")

# app.version(app.config.API_V1_STR)
# app.include_router(movies_router, prefix="/movies", tags=["movies"], dependencies=[Depends(app.mongodb_client.get_client())])
app.include_router(movies_router, prefix=app.config.API_V1_STR, tags=["v1"])


# print(app.routes)