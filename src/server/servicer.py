from data_provider.openapi_proxy import OpenAIProxy
from song_generator.song_generator_pb2 import MakeMeSuperstarRequest
from song_generator.song_generator_pb2_grpc import SongGeneratorServicer
from song_generator.base_pb2 import Album, Cover, Song


class SongGeneratorService(SongGeneratorServicer):
    def make_me_superstar(self, request: MakeMeSuperstarRequest, context) -> Album:
        cover = OpenAIProxy().create_album_cover(cover_description=str(request.cover_description))
        lyrics = OpenAIProxy().create_lyrics(
            song_theme=request.songs_theme,
            count=request.songs_count,
            music_category=request.category
        )
        titles = OpenAIProxy().create_titles(lyrics=lyrics)
        return Album(
            cover=self._transform_to_cover_domain(url=cover),
            songs=self._transform_to_songs_domain(lyrics=lyrics, titles=titles),
        )

    def _transform_to_songs_domain(self, lyrics: list[str], titles: list[str]) -> list[Song]:
        response = []
        for lyric, title in zip(lyrics, titles):
            response.append(
                Song(
                    title=title,
                    text=lyric,
                ),
            )
        return response

    def _transform_to_cover_domain(self, url: str) -> Cover:
        return Cover(url=url)

