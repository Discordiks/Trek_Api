from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
#модули для JWT токена
import auth_utils

router = APIRouter(
    prefix="/genre",
    tags=["genre"],
)

#получение списка жанров
@router.get('/', response_model=List[pyd.GenreBase])
async def get_genres(db:Session=Depends(get_db)):
    genres=db.query(models.Genre).all()
    return genres

#добавление жанров
@router.post('/', response_model=pyd.GenreBase)
async def create_genres(genre_input:pyd.GenreCreate, db:Session=Depends(get_db)):
    genres_db=models.Genre()
    genres_db.name=genre_input.name
    db.add(genres_db)
    db.commit()
    return genres_db

#редактирование жанров
@router.put('/{genre_id}', response_model=pyd.GenreBase)
async def update_genres(genre_id:int, genre_input:pyd.GenreCreate, db:Session=Depends(get_db)):
    genre_db=db.query(models.Genre).filter(models.Genre.id==genre_id).first()
    if not genre_db:
        raise HTTPException(status_code=404, detail="Жанр не найден!")
    genre_db.name=genre_input.name
    db.commit()
    return genre_db

#удаление жанров
@router.delete('/{genre_id}')
async def delete_genres(genre_id:int, db:Session=Depends(get_db)):
    genre_db=db.query(models.Genre).filter(models.Genre.id==genre_id).first()
    if not genre_db:
        raise HTTPException(status_code=404, detail="Жанр не найден!")
    db.delete(genre_db)
    db.commit()
    return "Жанр успешно удалён!"