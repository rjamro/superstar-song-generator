import logging
import os
from concurrent import futures

import grpc
from interceptors.logs import LoggingInterceptor
from servicer import SongGeneratorService

from song_generator.song_generator_pb2_grpc import \
    add_SongGeneratorServicer_to_server

logging.basicConfig(
    level=os.environ.get('LOGLEVEL', 'INFO'),
    format='%(levelname)s:\t%(asctime)s - %(message)s',
)


def main():
    interceptors = [LoggingInterceptor()]
    server = grpc.server(
        thread_pool=futures.ThreadPoolExecutor(max_workers=10),
        interceptors=interceptors,
    )
    add_SongGeneratorServicer_to_server(
        servicer=SongGeneratorService(),
        server=server,
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Listen to port 50051 [*]:')
    server.wait_for_termination()

if __name__ == '__main__':
    main()
