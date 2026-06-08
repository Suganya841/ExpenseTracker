from pydantic import BaseModel

class IncomeCreate(BaseModel):
    amount: int
    source: str
    date: str

class IncomeResponse(IncomeCreate):
    id: int

    class Config:
        from_attributes = True