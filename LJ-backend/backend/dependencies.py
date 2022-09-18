""" Starts a session for the DB call """

from pgsql.database import SessionLocal

def get_session():
    """ Creates a db session """
    try:
        _db = SessionLocal()
        return _db
    finally:
        _db.close()
