import logging

from contextlib import contextmanager
from pymongo import MongoClient

from .settings import Settings, settings

logger = logging.getLogger(__name__)

class Database:
    def __init__(self, settings: Settings):
        self._client = MongoClient(settings.MONGO_URL)
        self._db = self._client[settings.MONGO_DB_NAME]

    def get_db(self):
        return self._db

    @contextmanager
    def session(self):
        try:
            yield self._db
        except Exception:
            logger.exception("Session rollback because of exception")
            raise

db = Database(settings)