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
    prefix="/genre",
    tags=["genre"],
)

#получение списка жанров
@router.get('/', response_model=List[pyd.GenreBase])
async def get_genres(db:Session=Depends(get_db)):
    genres=db.query(models.Genre).all()
    return genres
