from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from core.config import DB_USER, DB_PASSWORD, DB_HOST

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/fastapi_practice"


Base = declarative_base()


class AsyncDatabaseSession:

    def __init__(self):
        self._engine = create_async_engine(
            SQLALCHEMY_DATABASE_URL,
            future=True,
            # echo=True,
        )

        self.session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )

    def __getattr__(self, name):
        return getattr(self.session(), name)

    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


db = AsyncDatabaseSession()


async def get_session():
    session = db.session()
    try:
        yield session
    finally:
        await session.close()
