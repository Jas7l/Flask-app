from pydantic import BaseModel


class PrintUser(BaseModel):
    orbis_id: int
    login: str
    active: bool

    class Config:
        from_attributes = True
