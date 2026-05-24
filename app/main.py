from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from loguru import logger

from app.config import get_settings
from app.database import engine, Base

from app.routers.auth import router as auth_router

settings = get_settings()

#lifespan: runs when app starts and stops
@asynccontextmanager
async def lifespan(app : FastAPI):
    logger.info(f"Starting {settings.APP_NAME}")

    #create table if not exists
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    logger.info("Database connected to tables and ready")
    yield
    logger.info("shutting down application")

#create fastapi app
app = FastAPI(
    title = settings.APP_NAME,
    description = "Personal Subscription Manager API",
    version = "1.0.0",
    lifespan = lifespan,
    docs_url = "/docs" if settings.DEBUG else None     
)

#CORS Middleware(allows frontend to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
@app.get("/")
async def root():
    return{
        "message" : "Welcome to SubTrackr API",
        "status" : "running"
    }