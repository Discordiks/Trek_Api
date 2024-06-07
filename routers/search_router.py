from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
#модули для JWT токена
import auth_utils

router = APIRouter(
    prefix="/search",
    tags=["search"],
)

#поиск песен по исполнителям
@router.get('/artist/{artist_name}', response_model=List[pyd.SongScheme])
async def get_artist_songs(artist_name: str, db:Session=Depends(get_db)):
    artist_db=db.query(models.Artist).filter(models.Artist.name==artist_name).first()
    if not artist_db:
        raise HTTPException(status_code=404, detail="Исполнитель не найден!")
    songs_db=db.query(models.Song).filter(models.Song.artists.contains(artist_db)).all()
    if songs_db ==[]:
        raise HTTPException(status_code=404, detail="У данного исполнителя пока нет ни одной песни!") 
    return songs_db

#поиск песен по жанрам
@router.get('/genre/{genre_name}', response_model=List[pyd.SongScheme])
async def get_genre_songs(genre_name: str, db:Session=Depends(get_db)):
    genre_db=db.query(models.Genre).filter(models.Genre.name==genre_name).first()
    if not genre_db:
        raise HTTPException(status_code=404, detail="Жанр не найден!")
    songs_db=db.query(models.Song).filter(models.Song.genres.contains(genre_db)).all()
    if songs_db == [] or songs_db == None:
        raise HTTPException(status_code=404, detail="Песен с данным жанром пока нет!") 
    return songs_db
