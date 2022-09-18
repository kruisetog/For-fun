""" Fixtures are functions that run before test cases when provided as dependency - Setup and tear-down """

import pytest
import psycopg2
from pgsql.database import host, database, port, username, password

base_url = 'http://127.0.0.1:8000/notifications/'

# used for Gql response status assertations
STATUS_OK = 200
STATUS_BAD_REQUEST = 400
STATUS_NOT_FOUND = 404
STATUS_UNPROCESSABLE_ENTITY = 422

@pytest.fixture
def supply_base_url():
    """ gets the base url for setup """
    yield base_url

def run_sql(query):
    """ runs the raw query in the data base """
    connection = psycopg2.connect(
            host=host,
            database=database,
            port=port,
            user=username,
            password=password
            )
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

@pytest.fixture
def cleanup_mock_in_db():
    """ deleting the last added row during testing from db """

    delete_query = "delete from notification"
    run_sql(delete_query)

# @pytest.fixture
# def reset_mock_in_db():
#     """ reset delete status to initial one """

#     update_aid_query = "update artifacts set status='policy not generated' where aid='F57F39464C814577BF302B2BA9A05FFA';"
#     run_sql(update_aid_query)
#     update_wid_query = "update artifacts set status='policy not generated' where wid='wid1';"
#     run_sql(update_wid_query)
