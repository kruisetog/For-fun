""" This file contains ORM structure and metadata """

from datetime import datetime
from sqlalchemy import Column, String, DateTime
from .database import Base


class Notification(Base):
    """ creates table in the database when the app boots """

    __tablename__ = 'notification'

    nid: str = Column(String, primary_key=True)
    uid: str = Column(String)
    aid: str = Column(String)
    wid: str = Column(String)
    type: str = Column(String)
    content: str = Column(String)
    importance: str = Column(String, default="low")
    email: str = Column(String)
    status: str = Column(String, default="unread")
    date_created: datetime = Column(DateTime, default=datetime.now)
    date_modified: datetime = Column(DateTime, default=datetime.now)
