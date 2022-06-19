from sqlalchemy.orm import Session


class CRUDbase:
    def __init__(self, model):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    async def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        """Get many entries from the database"""
        return db.query(self.model).offset(skip).limit(limit).all()

    async def get_by_uuid(self, db: Session, *, uuid: str):
        """Get entry from database by uuid"""
        return db.query(self.model).filter_by(user_uuid=uuid).first()

    async def remove(self, db: Session, *, uuid: int):
        """Remove entry from database by uuid"""
        obj = db.query(self.model).get(uuid)
        db.delete(obj)
        db.commit()
        return obj
