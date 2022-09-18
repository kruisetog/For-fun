""" Test cases for delete and merge mutations """

import json
from fastapi.testclient import TestClient
from main import app
from .mock_data import *
from .fixtures import *

client = TestClient(app)

def test_update_valid_notification(supply_base_url):
    for key, request in FAKE_DATA["valid_updates"].items():
        response = client.put(f'{supply_base_url}status',
                data=json.dumps(request), headers=HEADERS)
        assert response.status_code == STATUS_OK

def test_update_invalid_notification(supply_base_url):
    for key, request in FAKE_DATA["invalid_updates"].items():
        response = client.put(f'{supply_base_url}status',
                data=json.dumps(request), headers=HEADERS)
        assert response.status_code != STATUS_OK