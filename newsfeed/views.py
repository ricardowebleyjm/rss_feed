import feedparser
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


router = APIRouter()

router = APIRouter(
    prefix="/api/v1/newsfeed",
    tags=["newsfeed"],
    responses={404: {"description": "Not found"}},
)

def load_news_feed():
    gleaner_url = "http://www.jamaica-gleaner.com/feed/news.xml"
    feed = feedparser.parse(gleaner_url)
    entries = feed['entries']
    data = jsonable_encoder(entries)
    filtered_data = [
        {"title": item["title"], "link": item["link"], "summary": item["summary"], "id": item["id"], "published": item["published"],} for item in data
    ]
    return JSONResponse(content=filtered_data)