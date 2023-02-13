FROM python:3.11-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

WORKDIR /code

COPY client/main.py /code
COPY song_generator/ /code/song_generator
COPY client/requirements.txt /code

RUN python -m pip install -r requirements.txt

EXPOSE 8000
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]
