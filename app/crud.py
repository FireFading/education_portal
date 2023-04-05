from collections.abc import Iterable

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUD:
    async def create(self, db: AsyncSession):
        db.add(self)
        await db.flush()
        await db.commit()
        return self

    @classmethod
    async def search(cls, db: AsyncSession, kwargs: dict, order_by: str | None = None):
        filters = []
        for field, value in kwargs.items():
            try:
                if field.endswith("__gt"):
                    model_field = getattr(cls, field[:-4])
                    filters.append(model_field > value)
                elif field.endswith("__gte"):
                    model_field = getattr(cls, field[:-5])
                    filters.append(model_field >= value)
                elif field.endswith("__lt"):
                    model_field = getattr(cls, field[:-4])
                    filters.append(model_field < value)
                elif field.endswith("__lte"):
                    model_field = getattr(cls, field[:-5])
                    filters.append(model_field <= value)
                else:
                    model_field = getattr(cls, field)
                    filters.append(model_field == value)
            except AttributeError:
                return None
        query = select(cls).filter(and_(*filters))
        if order_by:
            order_by_field = getattr(cls, order_by[1:]).desc() if order_by[0] == "-" else None
            query = query.order_by(order_by_field)
        return await db.execute(query)

    @classmethod
    async def get(cls, db: AsyncSession, **kwargs):
        if result := await cls.search(db=db, kwargs=kwargs):
            return result.scalars().first()

    async def get_or_create(self, db: AsyncSession):
        cls = type(self)
        self_dict = {field: value for field, value in self.__dict__.items() if field != "_sa_instance_state"}
        instance = await cls.get(db=db, **self_dict)
        return instance or await self.create(db=db)

    @classmethod
    async def all(cls, db: AsyncSession):
        result = await db.execute(select(cls))
        return result.scalars().all()

    @classmethod
    async def filter(cls, db: AsyncSession, order_by: str | None = None, **kwargs):
        if result := await cls.search(db=db, order_by=order_by, kwargs=kwargs):
            return result.scalars().all()

    async def update(self, db: AsyncSession):
        await db.merge(self)
        await db.commit()

    @classmethod
    async def delete(cls, instances: list | object, db: AsyncSession):
        if isinstance(instances, Iterable):
            for instance in instances:
                await db.delete(instance)
        else:
            await db.delete(instances)
        await db.commit()
