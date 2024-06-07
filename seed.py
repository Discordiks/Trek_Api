from sqlalchemy.orm import Session
from database import engine
import models
from datetime import date

models.Base.metadata.drop_all(bind=engine) #пересоздание таблиц
models.Base.metadata.create_all(bind=engine) #пересоздание таблиц

with Session(bind=engine) as session:
    g1=models.Genre(name="Рок")
    g2=models.Genre(name="Поп")
    g3=models.Genre(name="Альтернатива")
    g4=models.Genre(name="Фонк")
    g5=models.Genre(name="K-pop")
    g6=models.Genre(name="Рэп")

    p1=models.Playlist(name="Для прохождения Бездны")
    p2=models.Playlist(name="Для чтения")
    p3=models.Playlist(name="Вечеринка")
    p4=models.Playlist(name="Жёсткое поедание пиццы")
    p5=models.Playlist(name="Подумать")

    a1=models.Artist(name="Lil Peep",birthday=date(2001,2,2))
    a2=models.Artist(name="Malinka", birthday=date(2002,1,1))
    a3=models.Artist(name="K/DA", birthday=date(2018,3,4))
    a4=models.Artist(name="Programmist", birthday=date(2003,3,4))

    s1=models.Song(name="Малиновое варенье", genres=[g1],playlists=[p1,p3],artists=[a2])
    s2=models.Song(name="Star Shopping", genres=[g6],playlists=[p5],artists=[a1])
    s3=models.Song(name="MORE", genres=[g2,g5],playlists=[p1,p3],artists=[a3])

    session.add_all([g1,g2,g3,g4,g5,g6,
                     p1,p2,p3,p4,p5,
                     a1,a2,a3,a4,
                     s1,s2,s3])
    session.commit()

