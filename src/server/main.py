from concurrent import futures
from servicer import SongGeneratorService
from song_generator.song_generator_pb2_grpc import add_SongGeneratorServicer_to_server
import grpc


def main():
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=10))
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
