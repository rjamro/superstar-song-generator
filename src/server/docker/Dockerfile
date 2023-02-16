FROM python:3.11-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

WORKDIR /code

COPY server/ /code
COPY song_generator/ /code/song_generator/
COPY certs/ /code/certs/

RUN python -m pip install -r requirements.txt

EXPOSE 50053
CMD [ "python", "main.py" ]
