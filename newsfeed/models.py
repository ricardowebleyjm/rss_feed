from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()


class NewsFeed(Base):
    __tablename__ = 'news_feed'
    id  = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    # rating = Column(Float)
    # time_created = Column(DateTime(timezone=True), server_default=func.now())
    # time_updated = Column(DateTime(timezone=True), onupdate=func.now())