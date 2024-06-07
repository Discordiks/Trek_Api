from pydantic import BaseModel, Field, EmailStr #какой формат данных хотим от пользователя
from typing import List
from datetime import date, datetime

class GenreCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Альтернатива")

class PlaylistCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Мощный заплыв")

class ArtistCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Lil Peep")
    birthday:date = Field(..., example='2001-01-01')

class UserCreate(BaseModel):
    mail:EmailStr = Field(...,example="lil_peep@mail.ru")
    password:str=Field(...,max_length=255, min_length=6,example="fafal1")

class SongCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Lil Peep")
    genre_id: List[int] = None #для добавления жанров через запятую
    playlist_id: List[int] = None 
    artist_id: List[int] = None 
