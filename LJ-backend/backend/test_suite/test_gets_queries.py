""" Test cases for get client """

from fastapi.testclient import TestClient
from main import app
from .mock_data import FAKE_DATA
from .fixtures import *

client = TestClient(app)

'''
Valid: Get notification based on uid, nid, or no supply (3 cases)
Invalid: Get notification without valid uid, nid, or with invalid argument supplied
'''

def test_get_valid_notification(supply_base_url):
    # get all notification
    r1 = client.get(f'{supply_base_url}')
    r2 = client.get(f'{supply_base_url}?nid={FAKE_DATA["valid_nids"]["valid1"]}')
    r3 = client.get(f'{supply_base_url}?uid={FAKE_DATA["valid_uid"]}')
    r4 = client.get(f'{supply_base_url}?nid={FAKE_DATA["valid_nids"]["valid3"]}&uid={FAKE_DATA["valid_uid"]}')
    assert r1.status_code == STATUS_OK
    assert r2.status_code == STATUS_OK
    assert all(key in ["nid", "uid", "aid", "wid", "type", "content", "importance",
        "importance", "email", "status", "date_created", "date_modified"]
        for key in list(r2.json().keys()))
    assert r3.status_code == STATUS_OK
    assert all(key in ["nid", "uid", "aid", "wid", "type", "content", "importance",
        "importance", "email", "status", "date_created", "date_modified"]
        for key in list(r3.json()[0].keys()))
    assert r4.status_code == STATUS_OK
    assert len(r4.json()) > 0


def test_invalid_get_notification(supply_base_url):
    r1 = client.get(f'{supply_base_url}?nid={FAKE_DATA["invalid_nid"]}')
    r2 = client.get(f'{supply_base_url}?uid={FAKE_DATA["invalid_uid"]}')
    r3 = client.post(f'{supply_base_url}?nid={FAKE_DATA["valid_nids"]["valid4"]}&uid={FAKE_DATA["invalid_uid"]}')
    assert r1.status_code == STATUS_NOT_FOUND
    assert r2.status_code == STATUS_OK
    assert r2.json() == []
    assert r3.status_code == STATUS_UNPROCESSABLE_ENTITY