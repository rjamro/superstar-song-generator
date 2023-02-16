from data_provider.openapi_proxy import OpenAIProxy
from song_generator.song_generator_pb2 import LyricsRequest, MakeMeSuperstarRequest
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

    def generate_lyrics(self, request: LyricsRequest, context) -> list[Song]:
        for _ in range(request.songs_count):
            lyrics = OpenAIProxy().create_lyrics(
                song_theme=request.songs_theme,
                count=1,
                music_category=request.category
            )
            titles = OpenAIProxy().create_titles(lyrics=lyrics)
            yield self._transform_to_song_domain(
                lyric=lyrics[0],
                title=titles[0],
            )

    def _transform_to_songs_domain(self, lyrics: list[str], titles: list[str]) -> list[Song]:
        response = []
        for lyric, title in zip(lyrics, titles):
            response.append(
                self._transform_to_song_domain(lyric=lyric, title=title)
            )
        return response

    def _transform_to_song_domain(self, lyric: str, title: str) -> Song:
        return Song(
            title=title,
            text=lyric,
        )

    def _transform_to_cover_domain(self, url: str) -> Cover:
        return Cover(url=url)

