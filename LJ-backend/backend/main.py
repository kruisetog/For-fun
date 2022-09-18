""" Main file that initializes the fastapi """

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pgsql.database import engine
from pgsql.models import Base
from service.routes import router as notification_router
from service.probes import router as probe_router

# table is created in DB
Base.metadata.create_all(bind=engine)

# args for swagger
app = FastAPI(title='FastAPI-GraphQL',
              description='GraphQL Artifact APIs', version='0.1')

origins = [
    'http://localhost:8080',
]
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(notification_router)
app.include_router(probe_router)
