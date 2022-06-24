from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from fastapi.exceptions import HTTPException


class CRUDbase:
    def __init__(self, model):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `_model`: A SQLAlchemy model class
        """
        self._model = model

    async def get_many(self, db: AsyncSession, skip: int = 0, limit: int = 100):
        """Get many entries from the database
        * `skip`: Number of entries to skip
        * `limit`: Maximum number of entries to return"""
        users = await db.execute(
            select(self._model).offset(skip).limit(limit)
        )
        return users.scalars().all()

    async def get_by_uuid(self, db: AsyncSession, uuid):
        """Get one entry from database by uuid
        * `uuid`: User uuid"""
        users = await db.execute(
            select(self._model)
            .where(self._model.uuid == uuid)
        )
        try:
            return users.scalar_one()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Not found")

    async def create_new(self, db: AsyncSession, obj):
        """Create new entry in database"""
        raise NotImplementedError

    async def remove(self, db: AsyncSession, uuid: int):
        """Remove entry from database by uuid
        * `uuid`: User uuid"""
        row = await self.get_by_uuid(db, uuid)
        await db.delete(row)
        await db.commit()
        return row
