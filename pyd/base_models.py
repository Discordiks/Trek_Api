from pydantic import EmailStr, BaseModel, Field #настройка валидации
from datetime import date, datetime

class GenreBase(BaseModel): #жанр аниме
    id:int=Field(...,gt=0,example=28) #обязательно к заполнению
    name:str=Field(...,example="Рок")

    class Config:
        orm_mode=True #наша модель будет легко соедняться с бд

class PlaylistBase(BaseModel):
    id:int=Field(...,gt=0,example=28) 
    name:str=Field(...,example="РОКЭНРОЛЛ")

    class Config:
        orm_mode=True 

class UserBase(BaseModel):
    id:int=Field(...,gt=0,example=228) 
    name:str=Field(...,example="Lil Peep")
    mail:EmailStr = Field(...,example="lil_peep@mail.ru")
    created_at:datetime=Field(...,example='2001-01-01 00:00:00')

    class Config:
        orm_mode=True 

class SongBase(BaseModel):
    id:int=Field(...,gt=0,example=228)
    name:str=Field(...,example="OVA")
    created_at:datetime=Field(...,example='2001-01-01 00:00:00')
    
    class Config:
        orm_mode=True 


