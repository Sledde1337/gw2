from sqlalchemy import Column, Integer, String
from database import Base

class Build(Base):
    __tablename__ = "builds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    profession = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    