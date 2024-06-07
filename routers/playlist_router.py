from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
#модули для JWT токена
import auth_utils

router = APIRouter(
    prefix="/playlist",
    tags=["playlist"],
)

#получение списка плейлистов
@router.get('/', response_model=List[pyd.PlaylistBase])
async def get_playlists(db:Session=Depends(get_db)):
    playlists=db.query(models.Playlist).all()
    return playlists

#добавление плейлистов
@router.post('/', response_model=pyd.PlaylistBase)
async def create_playlists(playlist_input:pyd.PlaylistCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    playlist_db=models.Playlist()
    playlist_db.name=playlist_input.name
    db.add(playlist_db)
    db.commit()
    return playlist_db

#редактирование плейлистов
@router.put('/{playlist_id}', response_model=pyd.PlaylistBase)
async def update_playlists(playlist_id:int, playlist_input:pyd.PlaylistCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    playlist_db=db.query(models.Playlist).filter(models.Playlist.id==playlist_id).first()
    if not playlist_db:
        raise HTTPException(status_code=404, detail="Плейлист не найден!")
    playlist_db.name=playlist_input.name
    db.commit()
    return playlist_db

#удаление плейлистов
@router.delete('/{playlist_id}')
async def delete_genres(playlist_id:int, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    playlist_db=db.query(models.Playlist).filter(models.Playlist.id==playlist_id).first()
    if not playlist_db:
        raise HTTPException(status_code=404, detail="Плейлист не найден!")
    db.delete(playlist_db)
    db.commit()
    return "Плейлист успешно удалён!"