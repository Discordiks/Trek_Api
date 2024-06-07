from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, DateTime, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship #связь между таблицами
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType, URLType
from sqlalchemy.sql import func

from database import Base

category=Table('song_genre', Base.metadata, #таблица, связывающая песни и жанры
               Column('song_id', ForeignKey('songs.id')),
               Column('genre_id', ForeignKey('genres.id'))
               )

category=Table('song_playlist', Base.metadata, #таблица, связывающая песни и плейлисты
               Column('song_id', ForeignKey('songs.id')),
               Column('playlist_id', ForeignKey('playlists.id'))
               )

category=Table('song_user', Base.metadata, #таблица, связывающая песни и исполнителей
               Column('song_id', ForeignKey('songs.id')),
               Column('user_id', ForeignKey('users.id'))
               )

class Genre (Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False)

class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False)
    #можно изображение подкинуть

class User(Base): 
    __tablename__ = "users"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False, unique=True)
    mail = Column(EmailType, nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at=Column(TIMESTAMP(timezone=False), 
                        server_default=func.now())

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False)
    created_at=Column(TIMESTAMP(timezone=False), 
                        server_default=func.now())
    
    genres=relationship("Genre", secondary='song_genre', backref='songs') #жанр
    playlists=relationship("Playlist", secondary='song_playlist', backref='songs') #плейлист
    users=relationship("User", secondary='song_user', backref='songs') #исполнитель



