# superstar-song-generator
Project is supposed to generate superstar songs using ChatGPT as a music producer and DALL-E as an album cover designer.

In fact it's just an educational app that presents usage of gRPC as a communication tool in microservices applications.

TODO:
- [X] Create basic app structure, that will be used as a basis for my presentation
- [ ] Create final app in case I will mess something up during demo :)
- [ ] Create presentation, that will summarize my research and consolidate knowledge about gRPC for me.
- [ ] Research
  - [X] Interceptors with metrics
  - [X] Interceptors with messages
  - [X] Another interesting interceptors
  - [X] Sentry integration (and other integrations)
  - [X] Read more about strategy/strategies used to send data (unary, bidirectional, client-streaming, server-streaming)
  - [X] Versioning proto files
  - [X] Splitting messages between multiple proto files


# Interceptors

## Metrics
Prometheus metrics https://pypi.org/project/py-grpc-prometheus/
OpenTelemetry metrics https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/grpc/grpc.html#opentelemetry-grpc-instrumentation
It looks like NewRelic has some support, as well. I can look at it at spare time.

## Logs
It looks like there is no library for that. However it can be easily implemented based on existing interceptors. Having basic interceptor we can choose whichever logging platform that satisfies our needs.

## Authentication Interceptor
SSL/TLS + Custom Header with token https://grpc.io/docs/guides/auth/#with-server-authentication-ssltls-and-a-custom-header-with-token


# Strategies
https://grpc.io/docs/what-is-grpc/core-concepts/#rpc-life-cycle

Generally all four strategies are available (unary, response-streaming, request-streaming, bidirectional streaming), **BUT** [Best Practices for Python](https://grpc.io/docs/guides/performance/#python) discourage developers to use streaming, as it creates more threads and makes it much slower than unary RPCs. Thank you GIL, once again :D

# Proto files
It is recommended to define widely used messages in [separate files](https://protobuf.dev/programming-guides/dos-donts/#do-define-widely-used-message-types-in-separate-files).
