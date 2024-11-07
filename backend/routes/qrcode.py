from fastapi import APIRouter
from models.qrcode_dto import QRCodeDTO
from typing import Any, Union
from routes import responses
from utils.errors import Error
from services import qrcode

router = APIRouter()

@router.post("/qrcode")
async def create_qrcode(args: QRCodeDTO):
    qr = await qrcode.create(args.url, args.creation_date)
    
    if isinstance(qrcode, Error):
        return responses.failure(qr, "QR code creation failed")
    
    return responses.success(qr)

@router.get("/qrcode/{id}")
async def find_qrcode(id: int):
    qr = await qrcode.find(id)
    
    if isinstance(qr, Error):
        return responses.failure(qr, "QR code not found")
    
    return responses.success(qr)
    