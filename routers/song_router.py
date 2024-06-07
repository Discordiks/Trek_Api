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

#добавление песен
@router.post('/', response_model=pyd.SongScheme)
async def create_songs(song_input:pyd.SongCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    songs_db=models.Song()
    songs_db.name=song_input.name
    #жанр
    for genre_id in song_input.genre_id:
        genre_db = db.query(models.Genre).filter(models.Genre.id==genre_id).first()
        if genre_db:
            songs_db.genres.append(genre_db)
        else:
            raise HTTPException(status_code=404, detail="Жанр не найден!")
    #плейлист
    for play_id in song_input.playlist_id:
        play_db = db.query(models.Playlist).filter(models.Playlist.id==play_id).first()
        if play_db:
            songs_db.playlists.append(play_db)
        else:
            raise HTTPException(status_code=404, detail="Плейлист не найден!")
    #исполнитель
    for art_id in song_input.artist_id:
        art_db = db.query(models.Artist).filter(models.Artist.id==art_id).first()
        if art_db:
            songs_db.artists.append(art_db)
        else:
            raise HTTPException(status_code=404, detail="Исполнитель не найден!")
    db.add(songs_db)
    db.commit()
    return songs_db

#редактирование песен
@router.put('/{song_id}', response_model=pyd.SongScheme)
async def update_songs(song_id:int, song_input:pyd.SongCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    songs_db=db.query(models.Song).filter(models.Song.id==song_id).first()
    if not songs_db:
        raise HTTPException(status_code=404, detail="Песня не найдена!")
    songs_db.name=song_input.name
    songs_db.genres.clear()
    songs_db.playlists.clear()
    songs_db.artists.clear()
    #жанр
    for genre_id in song_input.genre_id:
        genre_db = db.query(models.Genre).filter(models.Genre.id==genre_id).first()
        if genre_db:
            songs_db.genres.append(genre_db)
        else:
            raise HTTPException(status_code=404, detail="Жанр не найден!")
    #плейлист
    for play_id in song_input.playlist_id:
        play_db = db.query(models.Playlist).filter(models.Playlist.id==play_id).first()
        if play_db:
            songs_db.playlists.append(play_db)
        else:
            raise HTTPException(status_code=404, detail="Плейлист не найден!")
    #исполнитель
    for art_id in song_input.artist_id:
        art_db = db.query(models.Artist).filter(models.Artist.id==art_id).first()
        if art_db:
            songs_db.artists.append(art_db)
        else:
            raise HTTPException(status_code=404, detail="Исполнитель не найден!")
    db.add(songs_db)
    db.commit()
    return songs_db

#удаление песен
@router.delete('/{song_id}')
async def delete_songs(song_id:int, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    songs_db=db.query(models.Song).filter(models.Song.id==song_id).first()
    if not songs_db:
        raise HTTPException(status_code=404, detail="Песня не найдена!")
    db.delete(songs_db)
    db.commit()
    return "Удаление песни прошло успешно!"