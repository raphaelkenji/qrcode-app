from pydantic import BaseModel
from datetime import datetime

class QRCodeDTO(BaseModel):
    url: str
    creation_date: datetime