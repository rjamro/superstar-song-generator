# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import song_generator.base_pb2 as base__pb2
import song_generator.song_generator_pb2 as song__generator__pb2


class SongGeneratorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.make_me_superstar = channel.unary_unary(
                '/SongGenerator/make_me_superstar',
                request_serializer=song__generator__pb2.MakeMeSuperstarRequest.SerializeToString,
                response_deserializer=base__pb2.Album.FromString,
                )


class SongGeneratorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def make_me_superstar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SongGeneratorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'make_me_superstar': grpc.unary_unary_rpc_method_handler(
                    servicer.make_me_superstar,
                    request_deserializer=song__generator__pb2.MakeMeSuperstarRequest.FromString,
                    response_serializer=base__pb2.Album.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SongGenerator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SongGenerator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def make_me_superstar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SongGenerator/make_me_superstar',
            song__generator__pb2.MakeMeSuperstarRequest.SerializeToString,
            base__pb2.Album.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
