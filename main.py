from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from schemas import BuildCreate, BuildResponse
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GW2 Build Manager is running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/builds", response_model=BuildResponse)
def create_build(build: BuildCreate, db: Session = Depends(get_db)):
    db_build = models.Build(**build.dict())
    db.add(db_build)
    db.commit()
    db.refresh(db_build)
    return db_build

@app.get("/builds", response_model=list[BuildResponse])
def read_builds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Build).offset(skip).limit(limit).all()