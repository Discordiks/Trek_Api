from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
#модули для JWT токена
"""import auth_utils
from config import TokenInfo"""

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

#получение списка исполнителей
@router.get('/', response_model=List[pyd.UserBase])
async def get_users(db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    return users