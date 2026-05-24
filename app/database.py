from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.config import get_settings

settings = get_settings()

#create async database engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo = settings.DEBUG
)

#create session factory
AsyncSessionLocal = sessionmaker(
    bind = engine,
    class_ = AsyncSession,
    expire_on_commit= False
)

#Base class for all our models
class Base(DeclarativeBase):
    pass

#Dependancy to get database session
async def get_db():
    async with AsyncSessionLocal() as session:
        try: 
            yield session
        finally:
            await session.close()
            