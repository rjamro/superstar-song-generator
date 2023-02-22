import os

import grpc
from fastapi import FastAPI
from models.make_me_superstar import (Album, Song, SongsPayload,
                                      SuperstarPayload)

from song_generator.song_generator_pb2 import (LyricsRequest,
                                               MakeMeSuperstarRequest)
from song_generator.song_generator_pb2_grpc import SongGeneratorStub

app = FastAPI()

host = os.getenv('RESOURCE_SERVER')

def get_channel_credentials() -> grpc.ChannelCredentials:
    with open("certs/ca.pem", "rb") as fp:
        ca_cert = fp.read()

    return grpc.ssl_channel_credentials(ca_cert)

channel = grpc.aio.secure_channel(f'{host}:50053', credentials=get_channel_credentials())
client = SongGeneratorStub(channel=channel)


@app.post('/', response_model=Album)
async def superstar_album_generator(payload: SuperstarPayload) -> Album:
    grpc_payload = MakeMeSuperstarRequest(
        category=payload.category,
        songs_count=payload.songs_count,
        songs_theme=payload.songs_theme,
        cover_description=payload.cover_description,
    )

    response = await client.make_me_superstar(grpc_payload)

    return Album(
        cover_url=response.cover.url,
        songs=[Song(title=song.title, text=song.text) for song in response.songs]
    )


@app.post('/lyrics', response_model=list[Song])
async def superstar_album_generator(payload: SongsPayload) -> list[Song]:
    songs = []
    grpc_payload = LyricsRequest(
        category=payload.category,
        songs_count=payload.songs_count,
        songs_theme=payload.songs_theme,
    )

    async for song in client.generate_lyrics(grpc_payload):
        songs.append(Song(title=song.title, text=song.text))

    return songs
