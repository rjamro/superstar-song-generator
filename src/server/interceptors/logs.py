import logging
from typing import Any, Callable

import grpc
from grpc_interceptor.server import ServerInterceptor

logger = logging.getLogger(__file__)


class LoggingInterceptor(ServerInterceptor):
    def intercept(self, method: Callable, request: Any, context: grpc.ServicerContext, method_name: str) -> Any:
        logger.info('Request: {method}'.format(method=method_name))
        response = method(request, context)
        logger.info('Response: {status_code}'.format(status_code=context.code()))
        return response
