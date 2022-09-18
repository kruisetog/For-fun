""" This file defines data base connection details and exposes an engine and session object """

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
load_dotenv()
package = 'postgresql'
port = 5432

host = os.environ['POSTGRES_HOST']
username = os.environ['POSTGRES_USERNAME']
password = os.environ['POSTGRES_PASSWORD']
database = os.environ['POSTGRES_DB']

if os.environ.get('ENV_MODE') != '' and os.environ['ENV_MODE'] == 'test':
    # during pytest testclient runs in localhost from sql proxy
    host = 'localhost'

SQLALCHEMY_DATABASE_URL = f'{package}://{username}:{password}@{host}:{port}/{database}'
print('url: ', SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
