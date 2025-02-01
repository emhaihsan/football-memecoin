from pydantic import BaseModel


class MemeToken(BaseModel):
    name: str
    ticker: str
    shill_line: str
    headline: str
