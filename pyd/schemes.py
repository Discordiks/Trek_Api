from .base_models import *
from typing import List

class SongScheme(SongBase):
    genres:List[GenreBase] #жанры
    playlists:List[PlaylistBase] #плейлитсы
    users:List[UserBase] #исполнители
