import uvicorn

from src import App
from src import Settings
# from src import Router
# from src import Database


settings = Settings()
app = App(title="API", settings=settings)

app.create_database()
app.create_router()
# db = Database(settings)
# db.create_database()

# router = Router(app, settings)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="debug")
