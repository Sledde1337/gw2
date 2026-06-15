from pydantic import BaseModel

class BuildCreate(BaseModel):
    name: str
    profession: str
    description: str | None = None

class BuildResponse(BaseModel):
    id: int
    name: str
    profession: str
    description: str | None = None

    class Config:
        from_attributes = True
