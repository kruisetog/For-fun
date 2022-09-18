# SG-Service-Notification
Notification Service for Scribe rabbit dev v0.0.1

## To run server
Currently the server is deployed on solomon-ps-labs

Alternatively, to run it locally,
pip install -r backend/requirements.txt\
uvicorn main:app --reload
Backend server listening in http://localhost:8000

## Swagger UI
If you run the code below and visit your API’s root URL (http://localhost:8000/docs) you can view the automatically-generated Swagger UI documentation.

# Models

1. A Notification contains information about a notification to be sent to a user. The model for a user includes:
    - nid (the unique identifier of a user)
    - uid (uid of user the notification is sent to)
    - type (type of notification)
    - content (text of notification to be shown)
    - importance (Optional, importance (low, medium, high), default: low)
    - email (Optional, if notification to be sent to email)
    - wid (Optional, the workspace ID, wid, the notification is regarding)
    - aid (Optional, the artifact ID, wid, the notification is regarding)
    - date created, date modified

# Adding a notification from a service through NATS.IO

## Adding notification for a specific user
In the service the notification is coming from, publish the Nats.io message on the subject `scriberabbit.<SERVICE>.<action>`, with data following the newNotificationSchema schema:
    - Required: uid, type, content, status
    - Optional: importance, email, aid, wid

On main.py, add in the subject nats.io is supposed to listen on, with the callback `cb_create_notification_by_uid`
Example:
```
sub_placeholder_user_notif = await nc.subscribe("scriberabbit.SERVICE.event", cb=cb_create_notification_by_uid)
```

## Adding notifications for a users in a workspace
In the service the notification is coming from, publish the Nats.io message on the subject `scriberabbit.<SERVICE>.<action>`, with data following the newNotificationSchema schema:
    - Required: wid, type, content, status
    - Optional: importance, email, aid, uid
    
On main.py, add in the subject nats.io is supposed to listen on, with the callback `cb_create_notification_by_wid`
Example:
```
sub_placeholder_workspace_notif = await nc.subscribe("scriberabbit.SERVICE.action", cb=cb_create_notification_by_wid)
```

# Existing listeners/API

## Existing API

1. Get notifications (not deleted) by user id
    - Syntax: @router.get("/?uid={uid}")
    - Request type: GET
    - Parameter: uid as string to refer to the user being queried
    - Get the notifications based on the user id and are not deleted 

2. Update a notification status
    - Syntax: @router.put("/?status")
    - Request type: PUT
    - Parameter: UpdateStatusSchema Schema (nid, status)
    - Update the notification status

### Only for testing

Notifications should be added via Nats.IO which is the method of communication between backend services since users cannot directly create notification for other users. 

## Existing listeners

1. Create workspace notification for a new workspace user being added.
    - Subject: scriberabbit.workspace.notifAddWorkspaceUser
    - Callback: cb_create_notification_by_wid