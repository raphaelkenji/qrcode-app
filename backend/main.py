from databases import Database
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from adapters import database
from utils import services, settings
from contextlib import asynccontextmanager
from routes.qrcode import router

import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    services.database = Database(
        database.dsn(
            settings.DB_DRIVER,
            settings.DB_USER,
            settings.DB_PASS,
            settings.DB_HOST,
            settings.DB_PORT,
            settings.DB_NAME
        )
    )
    await services.database.connect()
    yield
    await services.database.disconnect()
        
app = FastAPI(lifespan=lifespan)
app.include_router(router)
app.mount("/uploads", app=StaticFiles(directory="Uploads"), name="uploads")

if __name__ == "__main__":
    uvicorn.run("main:app")