from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date
import models
from database import get_db
import pyd
import random, string
#модули для JWT токена
import auth_utils

router = APIRouter(
    prefix="/artist",
    tags=["artist"],
)

#получение списка исполнителей
@router.get('/', response_model=List[pyd.ArtistBase])
async def get_artists(db:Session=Depends(get_db)):
    artists=db.query(models.Artist).all()
    return artists

#добавление исполнителей
@router.post('/', response_model=pyd.ArtistBase)
async def create_artists(artist_input:pyd.ArtistCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    artists_db=db.query(models.Artist).filter(models.Artist.name==artist_input.name).first()
    if artists_db:
        raise HTTPException(400, 'Никнейм занят!')
    artists_db=models.Artist()
    artists_db.name=artist_input.name
    if artist_input.birthday >= date.today():
        raise HTTPException(400, 'Ты ещё не родился!')
    artists_db.birthday=artist_input.birthday
    db.add(artists_db)
    db.commit()
    return artists_db

#редактирование исполнителей
@router.put('/{artist_id}', response_model=pyd.ArtistBase)
async def update_artists(artist_id:int, artist_input:pyd.ArtistCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    artists_db=db.query(models.Artist).filter(models.Artist.id==artist_id).first()
    if not artists_db:
        raise HTTPException(status_code=404, detail="Исполнитель не найден!")
    art_db=db.query(models.Artist).filter(models.Artist.name==artist_input.name).first() #ввёл никнейм
    art_db_1=db.query(models.Artist).where(models.Artist.name==artists_db.name).first() #никнейм в дб равен никнейму исполнителя, что сейчас редактируется
    if art_db:
        if art_db.name and art_db.name != art_db_1.name:
            raise HTTPException(400, 'Никнейм занят!')
    artists_db.name=artist_input.name
    if artist_input.birthday >= date.today():
        raise HTTPException(400, 'Ты ещё не родился!')
    artists_db.birthday=artist_input.birthday
    db.commit()
    return artists_db

#удаление исполнителей
@router.delete('/{artist_id}')
async def delete_artists(artist_id:int, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    artists_db=db.query(models.Artist).filter(models.Artist.id==artist_id).first()
    if not artists_db:
        raise HTTPException(status_code=404, detail="Исполнитель не найден!")
    db.delete(artists_db)
    db.commit()
    return "Исполнитель успешно удалён!"