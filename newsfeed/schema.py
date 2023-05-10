from pydantic import BaseModel

class NewsFeed(BaseModel):
    title: str
    # rating: int
    class Config:
        orm_mode = True