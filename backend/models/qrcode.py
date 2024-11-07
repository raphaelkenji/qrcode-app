from pydantic import BaseModel
from datetime import datetime

class QRCode(BaseModel):
    id: int
    url: str
    path: str
    creation_date: datetime