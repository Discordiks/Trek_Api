from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import pyd
from typing import List
from routers import genre_router, playlist_router, song_router, user_router, artist_router, search_router

app = FastAPI()

# подключение АпиРоутера (маршруты сущности)
app.include_router(user_router)
app.include_router(artist_router)
app.include_router(genre_router)
app.include_router(playlist_router)
app.include_router(song_router)
app.include_router(search_router)
