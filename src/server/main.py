import asyncio
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

def get_server_credentials() -> grpc.ServerCredentials:
    with open("certs/server.key", "rb") as fp:
        server_key = fp.read()
    with open("certs/server.pem", "rb") as fp:
        server_cert = fp.read()

    return grpc.ssl_server_credentials(
        private_key_certificate_chain_pairs=[(server_key, server_cert)],
    )


async def main():
    # interceptors = [LoggingInterceptor()]
    server = grpc.aio.server(
        migration_thread_pool=futures.ThreadPoolExecutor(max_workers=10),
        # interceptors=interceptors,
    )
    add_SongGeneratorServicer_to_server(
        servicer=SongGeneratorService(),
        server=server,
    )
    server.add_secure_port('[::]:50053', server_credentials=get_server_credentials())
    await server.start()
    print('Listen to port 50053 [*]:')
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(main())
