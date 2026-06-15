from fastapi import FastAPI
from pydantic import BaseModel
from database import Base, engine
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

class Build(BaseModel):
    name: str
    profession: str
    description: str | None = None

builds = []

@app.get("/")
def root():
    return {"message": "GW2 Build Manager is running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/builds")
def create_build(build: Build):
    builds.append(build)
    return build

@app.get("/builds")
def get_builds():
    return builds

