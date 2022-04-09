from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from endpoints import button, websockets
from core.config import settings

#
app = FastAPI(openapi_prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(
    button.router,
    prefix='/button',
    tags=['Get data from button'],
)

app.include_router(
    websockets.router,
    tags=['Websockets connection'],
)
