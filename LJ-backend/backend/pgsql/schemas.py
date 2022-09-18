""" This file contains the gql schema """

from typing import Optional
from pydantic import BaseModel


class ResponseSchema(BaseModel):
    """ schema for any response """
    nid: str
    uid: str
    wid: str
    aid: str
    type: str
    content: str
    importance: str
    status: str
    email: str

    date_created: str
    date_modified: str

    class Config:
        """ auto enable orm"""
        orm_mode = True


class newNotificationSchema(BaseModel):
    """ schema for creating a new notification for a specific user """
    uid: str
    type: str
    content: str
    status: str
    importance:  Optional[str]
    email:  Optional[str]
    aid:  Optional[str]
    wid: Optional[str]

    class Config:
        """ auto enable orm"""
        orm_mode = True
# when invite accept and created


class newWorkspaceNotificationSchema(BaseModel):
    """ schema for creating a new notification for a workspace"""
    uid: Optional[str]
    type: str
    content: str
    status: str
    importance:  Optional[str]
    email:  Optional[str]
    aid:  Optional[str]
    wid: str

    class Config:
        """ auto enable orm"""
        orm_mode = True


class UpdateStatusSchema(BaseModel):
    """ schema for uploading a new invite"""
    nid: str
    status: str

    class Config:
        """ auto enable orm"""
        orm_mode = True


class pubDict(BaseModel):
    """ publishing a message """
    sub: str
    msg: dict
