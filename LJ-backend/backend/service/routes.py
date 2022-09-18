""" This file routes the url to the corresponding requests handlers """

import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from dependencies import get_session

from pgsql.schemas import UpdateStatusSchema, newNotificationSchema
from .crud import get_all_notifications, get_notification_by_nid, get_notifications_by_uid, update_notification_status, new_notification, new_workspace_notification

load_dotenv()
bucket_name = os.environ.get('BUCKET')

router = APIRouter(
    prefix='/notifications',
    tags=['notifications'],
    dependencies=[Depends(get_session)],
    responses={404: {'description': 'Not found'}}
)


@router.get("/")
async def get_notifications(nid: str = '', uid: str = ''):
    """ route for getting all notifications (TESTING ONLY), a notification with aid, notifications with wid """
    if nid != '':
        return get_notification_by_nid(db=get_session(), nid=nid)
    elif uid != '':
        return get_notifications_by_uid(db=get_session(), uid=uid)
    # else:
    #     return get_all_notifications(db=get_session())


@router.put('/status')
def update_notification(request: UpdateStatusSchema):
    """ route for updating status; called from workflow """
    status_details = request.dict()
    response = update_notification_status(
        db=get_session(), notification_info=status_details)
    return response


@router.post('/')
def create_notification(notification: newNotificationSchema):
    """ route for creating a single notification """
    notification_details = notification.dict()
    response = new_notification(
        db=get_session(), notification_info=notification_details)
    return response
