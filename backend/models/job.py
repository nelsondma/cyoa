from sqlalchemy import Column, Integer, String, DateTime #These are the columns that will be used to create the database tables
from sqlalchemy.sql import func #This is the function that will be used to create the database tables


from db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"


    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, index=True, unique=True)
    session_id = Column(String, index=True)
    theme = Column(String)
    status = Column(String)
    story_id = Column(Integer, nullable=True)
    error = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)

