#sqlalchemy is a library that allows us to interact with the database using Python objects instead of writing raw SQL queries. It takes in python and translates it into sql queries.
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON #These are the columns that will be used to create the database tables
from sqlalchemy.sql import func #This is the function that will be used to create the database tables
from sqlalchemy.orm import relationship #This is the function that will be used to create the relationships between the database tables
from db.database import Base #This is the base class that will be used to create the database tables

#We have an overaching story model contianing the metadata for the story, such as the title, session_id, and the creation date.
class Story(Base):
    __tablename__ = "stories"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    session_id = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    nodes = relationship("StoryNode", back_populates="story") 

#Now we have the nodes for the story, like every possible path the story can take.
class StoryNode(Base):
    __tablename__ = "story_nodes"
    
    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id"), index=True)
    content = Column(String)
    is_root = Column(Boolean, default=False)
    is_ending = Column(Boolean, default=False)
    is_winning_ending = Column(Boolean, default=False)
    options = Column(JSON, default=list)

    story = relationship("Story", back_populates="nodes")
