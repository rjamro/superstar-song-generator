from fastapi import FastAPI
import os

import grpc
from models.make_me_superstar import Album, Song, SuperstarPayload
from song_generator.song_generator_pb2_grpc import SongGeneratorStub
from song_generator.song_generator_pb2 import MakeMeSuperstarRequest

app = FastAPI()

host = os.getenv('RESOURCE_SERVER')
channel = grpc.insecure_channel(f'{host}:50051')
client = SongGeneratorStub(channel=channel)


@app.post('/', response_model=Album)
def superstar_album_generator(payload: SuperstarPayload) -> Album:
    payload = MakeMeSuperstarRequest(
        category=payload.category,
        songs_count=payload.songs_count,
        songs_theme=payload.songs_theme,
        cover_description=payload.cover_description,
    )

    response = client.make_me_superstar(payload)

    return Album(
        cover_url=response.cover.url,
        songs=[Song(title=song.title, text=song.text) for song in response.songs]
    )
