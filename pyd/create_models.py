from pydantic import BaseModel, Field, EmailStr #какой формат данных хотим от пользователя
from typing import List

class GenreCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Альтернатива")

class PlaylistCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Мощный заплыв")

class UserCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Lil Peep")
    mail:EmailStr = Field(...,example="lil_peep@mail.ru")
    password:str=Field(...,max_length=255, min_length=6,example="fafal1")
    type_id:int=Field(..., gt=0, example=10)

class SongCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Lil Peep")
    genre_id: List[int] = None #для добавления жанров через запятую
    playlist_id: List[int] = None 
    user_id: List[int] = None 
