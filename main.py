from fastapi import FastAPI

from routers import news_feed
from db.db_session import SessionLocal

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(news_feed.router)
