from contextlib import contextmanager
import logging

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from pymongo import MongoClient

from .settings import Settings

logger = logging.getLogger(__name__)

Base = declarative_base()

class DatabaseSQLAlchemy:
    
    def __init__(self, settings: Settings):
        self._engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
        self._session_factory = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

    def create_database(self):
        Base.metadata.create_all(self._engine)

    @classmethod
    @contextmanager
    def session(self):
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()

class DatabaseNoSQL:
    
    def __init__(self, settings: Settings):
        self._client = MongoClient(settings.MONGODB_URL)
        self._db = self._client[settings.MONGODB_NAME]

    def create_database(self):
        pass

    @classmethod
    @contextmanager
    def session(self):
        try:
            yield self._db
        except Exception:
            logger.exception("Session rollback because of exception")
            raise