from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
#модули для JWT токена
import auth_utils

router = APIRouter(
    prefix="/song",
    tags=["song"],
)

#получение списка песен
@router.get('/', response_model=List[pyd.SongScheme])
async def get_songs(db:Session=Depends(get_db)):
    songs=db.query(models.Song).all()
    return songs