from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.users import User as m_User
from app.schemas.users import CreateUser, LoginCredentials, ShowUser
from app.utils.messages import messages
from app.utils.password import get_hashed_password, verify_password

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register/", status_code=status.HTTP_201_CREATED, summary="Create user")
async def register(user: CreateUser, db: AsyncSession = Depends(get_session)) -> ShowUser:
    db_user = await m_User(
        name=user.name,
        surname=user.surname,
        email=user.email,
        password=get_hashed_password(user.password),
    ).create(db=db)
    return ShowUser.from_orm(db_user).dict() if user else None


@router.get("/login/", status_code=status.HTTP_200_OK, summary="Login")
async def login(
    user: LoginCredentials,
    db: AsyncSession = Depends(get_session),
):
    db_user = await m_User.get(db=db, email=user.email)
    if not verify_password(password=user.password, hashed_password=db_user):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=messages.WRONG_PASSWORD)
    return db_user
