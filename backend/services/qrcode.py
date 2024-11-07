from datetime import datetime
from typing import Any, Union
from utils.errors import Error
from utils.validation import validate_url
from utils import services, settings

import os
import qrcode
from pathlib import Path

UPLOADS_DIR = Path("Uploads")
READ_PARAMS = "id, url, path, creation_date"

async def create(url: str, creation_date: datetime) -> Union[dict[str, Any], Error]:
    if not validate_url(url):
        return Error.INVALID_URL
    
    qr = qrcode.make(url)
    
    if qr is None:
        return Error.QRCODE_CREATION_FAILED
    
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    
    file_name = f"{creation_date.strftime('%Y-%m-%d_%H-%M-%S')}.png"
    file_path = UPLOADS_DIR / file_name
    
    qr.save(file_path, "PNG")
    
    qr_url = f"{settings.API_URL}/uploads/{file_name}"
    
    qr_submit = await services.database.fetch_one(
        query=f"""
            INSERT INTO qrcodes (url, path, creation_date)
            VALUES (:url, :path, :creation_date)
            RETURNING {READ_PARAMS}
        """,
        values={
            "url": url,
            "path": qr_url,
            "creation_date": creation_date
        }
    )
    
    if qr_submit is None:
        return Error.QRCODE_SUBMISSION_FAILED
    
    return dict(qr_submit._mapping.items())

async def find(id: int) -> Union[dict[str, Any], Error]:
    qr = await services.database.fetch_one(
        query=f"""
            SELECT {READ_PARAMS}
            FROM qrcodes
            WHERE id = :id
        """,
        values={"id": id}
    )
    
    if qr is None:
        return Error.QRCODE_READ_FAILED
    
    return dict(qr._mapping.items())
