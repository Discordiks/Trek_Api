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

    p1=models.Playlist(name="Для прохождения Бездны")
    p2=models.Playlist(name="Для чтения")
    p3=models.Playlist(name="Вечеринка")
    p4=models.Playlist(name="Жёсткое поедание пиццы")

    a1=models.Artist(name="Lil Peep",birthday=date(2001,2,2))
    a2=models.Artist(name="Malinka", birthday=date(2002,1,1))

    s1=models.Song(name="Малиновое варенье", genres=[g1],playlists=[p1,p3],artists=[a2] )

    session.add_all([g1,g2,g3,g4,g5,
                     p1,p2,p3,p4,
                     a1,a2,
                     s1])
    session.commit()

