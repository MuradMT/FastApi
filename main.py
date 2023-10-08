from fastapi import FastAPI
from database import db

app=FastAPI()
database=db

@app.get("/")
async def root():
    return {"Hello":"World"}
@app.get("/api/v1/users")
async def fetch_users():
    return database
