""" Test cases for post and put mutations """

import json
from fastapi.testclient import TestClient
from main import app
from .mock_data import HEADERS, FAKE_DATA
from .fixtures import *

client = TestClient(app)

@pytest.mark.order(1)
def test_create_valid_notifiaction(supply_base_url):
    for key, request in FAKE_DATA["valid_notification_posts"].items():
        response = client.post(f'{supply_base_url}',
                    data=json.dumps(request), headers=HEADERS)
        assert response.status_code == STATUS_OK
        FAKE_DATA["valid_nids"][key] = response.json()["nid"]
    FAKE_DATA["valid_updates"]["valid_update_1"]["nid"] = FAKE_DATA["valid_nids"]["valid1"]
    FAKE_DATA["valid_updates"]["valid_update_2"]["nid"] = FAKE_DATA["valid_nids"]["valid2"]


@pytest.mark.order(2)
def test_invalid_create_notification(supply_base_url):
    for key, request in FAKE_DATA["invalid_notification_posts"].items():
        response = client.post(f'{supply_base_url}',
                    data=json.dumps(request), headers=HEADERS)
        print(response.status_code)
        assert response.status_code != STATUS_OK