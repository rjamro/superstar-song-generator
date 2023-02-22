import logging
from typing import Any, Callable

import grpc

logger = logging.getLogger(__file__)


class LoggingInterceptor(grpc.aio.ServerInterceptor):
    async def intercept(self, method: Callable, request: Any, context: grpc.ServicerContext, method_name: str) -> Any:
        logger.info('Request: {method}'.format(method=method_name))
        response = method(request, context)
        logger.info('Response: {status_code}'.format(status_code=context.code()))
        return response

    async def intercept_service(self, continuation, handler_call_details):
        """Implementation of grpc.ServerInterceptor.

        This is not part of the grpc_interceptor.ServerInterceptor API, but must have
        a public name. Do not override it, unless you know what you're doing.
        """
        next_handler = continuation(handler_call_details)
        handler_factory, next_handler_method = _get_factory_and_method(next_handler)

        async def invoke_intercept_method(request, context):
            method_name = handler_call_details.method
            return await self.intercept(next_handler_method, request, context, method_name,)

        return handler_factory(
            invoke_intercept_method,
            request_deserializer=next_handler.request_deserializer,
            response_serializer=next_handler.response_serializer,
        )


def _get_factory_and_method(
    rpc_handler: grpc.RpcMethodHandler,
) -> tuple[Callable, Callable]:
    if rpc_handler.unary_unary:
        return grpc.unary_unary_rpc_method_handler, rpc_handler.unary_unary
    elif rpc_handler.unary_stream:
        return grpc.unary_stream_rpc_method_handler, rpc_handler.unary_stream
    elif rpc_handler.stream_unary:
        return grpc.stream_unary_rpc_method_handler, rpc_handler.stream_unary
    elif rpc_handler.stream_stream:
        return grpc.stream_stream_rpc_method_handler, rpc_handler.stream_stream
    else:  # pragma: no cover
        raise RuntimeError("RPC handler implementation does not exist")
