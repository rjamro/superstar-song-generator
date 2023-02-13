from fastapi import FastAPI
import os

app = FastAPI()

host = os.getenv('RESOURCE_SERVER')


@app.get('/')
def superstar_album_generator():
    return 'This is a placeholder'
