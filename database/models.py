# database/models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Photo(Base):
    __tablename__ = 'photos'
    
    id = Column(Integer, primary_key=True)
    filename = Column(String(255), unique=True)
    filepath = Column(String(500))
    caption = Column(Text)
    hashtags = Column(Text)
    status = Column(String(20))  # pending, approved, posted, failed
    scheduled_time = Column(DateTime)
    posted_time = Column(DateTime)
    instagram_post_id = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)