""" This file handles database calls """

import uuid
from datetime import datetime
from sqlalchemy import and_
from sqlalchemy.orm.session import Session
from fastapi import HTTPException
from pgsql.models import Notification
from pgsql.schemas import newNotificationSchema, UpdateStatusSchema


def get_all_notifications(db: Session):
    """ gets all the notifications from the database. should only be used for testing """

    try:
        return db.query(Notification).all()

    except Exception as err:
        raise err


def get_notifications_by_uid(db: Session, uid: str):
    """ gets the notifications for the given wid """

    try:
        return db.query(Notification).filter(and_(Notification.uid == uid, Notification.status != "deleted")).all()

    except Exception as err:
        raise err


def get_notification_by_nid(db: Session, nid: str):
    """ gets the notifications for the given nid """

    try:
        target = db.query(Notification).filter(
            Notification.nid == nid).one_or_none()
        if target is None:
            raise HTTPException(
                status_code=404, detail='notification nid does not exist')
        return target

    except Exception as err:
        raise err


def new_notification(db: Session, notification_info: newNotificationSchema):
    """ posts a single notification to the database """
    try:
        notification_entity = Notification(**notification_info)
        notification_entity.nid = str(uuid.uuid4().hex.upper())
        notification_entity.date_created = datetime.now()
        print('notification: ', notification_entity)
        db.add(notification_entity)
        db.commit()

        return db.query(Notification).filter(
            Notification.nid == notification_entity.nid).one()

    except Exception as err:
        db.rollback()
        raise err


def new_workspace_notification(db: Session, notification_info: newNotificationSchema, workspaceUsers):
    """ creates notifications based on users in the workspace to the database """
    try:
        response = notification_info.copy()
        response["uid_sent_to"] = []
        for workspaceUser in workspaceUsers:
            notification_entity = Notification(**notification_info)
            notification_entity.nid = str(uuid.uuid4().hex.upper())

            notification_entity.uid = workspaceUser["uid"]
            notification_entity.date_created = datetime.now()
            response["notification_users"].append(workspaceUser["uid"])
            db.add(notification_entity)
            db.commit()

        return response

    except Exception as err:
        db.rollback()
        raise err


def update_notification_status(db: Session, notification_info: UpdateStatusSchema):
    """ updates the status of the notification """

    try:

        notification_in_db = db.query(Notification).filter(
            Notification.nid == notification_info['nid']).one_or_none()

        if notification_in_db is not None:
            notification_in_db.status = notification_info['status']
            notification_in_db.date_modified = datetime.now()
            db.commit()
            return db.query(Notification).filter(
                Notification.nid == notification_info['nid']).one()
        raise HTTPException(
            status_code=404, detail='notification nid does not exist to update')

    except Exception as err:
        db.rollback()
        raise err
