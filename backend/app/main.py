from fastapi import FastAPI
from .db.database import create_table
from .db import models

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SlipSync backend is running"}

create_table()