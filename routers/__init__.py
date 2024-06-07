# в этом файле подключаются все маршрутизаторы апи, у каждого меняется название
from .artist_router import router as artist_router
from .genre_router import router as genre_router
from .playlist_router import router as playlist_router
from .song_router import router as song_router
from .user_router import router as user_router
from .search_router import router as search_router