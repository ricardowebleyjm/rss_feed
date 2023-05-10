from fastapi import APIRouter
from newsfeed import views

router = APIRouter()

router = APIRouter(
    prefix="/api/v1/newsfeed",
    tags=["newsfeed"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def news_feed():
    """Returns a list of the latest news"""
    feed = views.load_news_feed()
    return feed