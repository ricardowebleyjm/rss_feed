from fastapi import FastAPI

from routers import news_feed

app = FastAPI()


app.include_router(news_feed.router)
