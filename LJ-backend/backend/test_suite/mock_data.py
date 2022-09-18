""" This file contains mock data used in test cases based on localhost db
NOTE: Please Don't change the data in Dev SQL DB """

HEADERS = {'Content-Type': 'application/json'}


'''
'''
FAKE_DATA = {
    "valid_nids": {
        "valid1": "",
        "valid2": "",
        "valid3": "",
        "valid4": "",
        "valid5": ""
    },
    "invalid_nid": "this_is_not_an_id",
    "valid_uid": "test-user",
    "invalid_uid": "invalid-user",

    "valid_notification_posts": {
        "valid1": {
            "uid": "test-user",
            "type": "another-type",
            "content": "This is another notification",
            "status": "unread",
            "importance": "low",
            "email": "random_email@outlook.com",
            "aid": "another-aid",
            "wid": "random-wid"
        },
        "valid2": {
            "uid": "another-user",
            "type": "test-type",
            "content": "This is a random notification",
            "status": "unread",
        },
        "valid3": {
            "uid": "test-user",
            "type": "random-type",
            "content": "This is a notification",
            "status": "unread",
            "importance": "high",
            "email": "test_email@outlook.com",
            "aid": "test-aid",
            "wid": "test-wid"
        },
        "valid4": {
            "uid": "test-user",
            "type": "random-type",
            "content": "This is a notification",
            "status": "unread",
            "importance": "high",
            "email": "test_email@outlook.com",
            "aid": "test-aid",
            "wid": "test-wid"
        },
        "valid5": {
            "uid": "test-user",
            "type": "random-type",
            "content": "This is a notification",
            "status": "unread",
            "importance": "high",
            "email": "test_email@outlook.com",
            "aid": "test-aid",
            "wid": "test-wid"
        }
    },
    "invalid_notification_posts": {
        # lacking a compulsory field
        "missing_field": {
            "uid": "test-user",
            "type": "random-type",
            "status": "unread",
            "importance": "high",
            "email": "test_email@outlook.com",
            "aid": "test-aid",
            "wid": "test-wid"
        },
        # invalid key name
        "invalid_key": {
            "kid": "test-user",
            "type": "random-type",
            "content": "This is a notification",
            "status": "unread",
            "importance": "high",
            "email": "test_email@outlook.com",
            "nid": "test-aid",
            "rid": "test-wid"
        }
    },
    "valid_updates": {
        "valid_update_1": {
            "nid": "",
            "status": "read"
        },
        "valid_update_2": {
            "nid": "",
            "status": "deleted"
        }
    },
    "invalid_updates": {
        "missing_field": {
            "nid": ""
        },
        "redundant_field": {
            "nid": "",
            "status": "read",
            "something": "This is something"
        },
        "invalid_nid": {
            "nid": "invalid_nid",
            "status": "deleted"
        }
    }
}
