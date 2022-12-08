""" Driver program for application """
from API.Episodes import models, views
from engine.db import engine, sessionmaker
from fastapi import FastAPI


models.Base.metadata.create_all(bind=engine)

sessionmaker = sessionmaker(bind=engine)

session = sessionmaker()

app = FastAPI()

app.include_router(views.router)
