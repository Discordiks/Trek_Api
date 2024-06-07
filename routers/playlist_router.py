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
    prefix="/playlist",
    tags=["playlist"],
)

#получение списка плейлистов
@router.get('/', response_model=List[pyd.PlaylistBase])
async def get_playlists(db:Session=Depends(get_db)):
    playlists=db.query(models.Playlist).all()
    return playlists