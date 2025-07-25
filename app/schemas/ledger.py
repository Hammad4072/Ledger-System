from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class LedgerBase(BaseModel):
    title: str
    amount: float
    type: str

class LedgerDisplay(LedgerBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
