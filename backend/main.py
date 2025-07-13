# app/main.py

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from dotenv import load_dotenv
load_dotenv(".env")

from core.config import config
from api.v1 import users, auth  # примерные роутеры
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("easympnn")


app = FastAPI(
    title=config.PROJECT_NAME,
    version="1.0.0"
)
app.mount("/static", StaticFiles(directory="static"), name="static")
# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])




# # Событие остановки
# @app.on_event("shutdown")
# async def shutdown_event():
#     pass  # закрытие соединений или очистка ресурсов, если нужно


if __name__ == "__main__":
    if config.DEBUG:
        logger.setLevel(logging.DEBUG)
        uvicorn.run("main:app",
            host=config.SERVER_HOST,
            port=config.SERVER_PORT,
            reload=True,
            ssl_keyfile=config.SSL_KEYFILE,
            ssl_certfile=config.SSL_CERTFILE
        )
    else:
        logger.setLevel(logging.INFO)
        uvicorn.run("main:app",
            host=config.SERVER_HOST,
            port=config.SERVER_PORT
        )