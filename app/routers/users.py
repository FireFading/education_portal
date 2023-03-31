from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.users import CreateUser, ShowUser
from app.database import get_session
from app.models.users import User as m_User
from app.crud.users import DBUsers


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", status_code=status.HTTP_201_CREATED, summary="Create statistic")
async def register(user: CreateUser, db: AsyncSession = Depends(get_session)) -> ShowUser:
    new_user = m_User(
        name=user.name,
        surname=user.surname,
        email=user.surname
    )
    db_user = await DBUsers.create(db=db, user=new_user)
    return ShowUser.from_orm(db_user).dict() if user else None
