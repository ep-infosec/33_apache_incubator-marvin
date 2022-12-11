# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

# from .actions_pb2 import * /python3
# import actions_pb2 as actions__pb2 /python2
from ..stubs import actions_pb2 as actions__pb2


class OnlineActionHandlerStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self._remote_execute = channel.unary_unary(
            '/OnlineActionHandler/_remote_execute',
            request_serializer=actions__pb2.OnlineActionRequest.SerializeToString,
            response_deserializer=actions__pb2.OnlineActionResponse.FromString,
        )
        self._remote_reload = channel.unary_unary(
            '/OnlineActionHandler/_remote_reload',
            request_serializer=actions__pb2.ReloadRequest.SerializeToString,
            response_deserializer=actions__pb2.ReloadResponse.FromString,
        )
        self._health_check = channel.unary_unary(
            '/OnlineActionHandler/_health_check',
            request_serializer=actions__pb2.HealthCheckRequest.SerializeToString,
            response_deserializer=actions__pb2.HealthCheckResponse.FromString,
        )


class OnlineActionHandlerServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def _remote_execute(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def _remote_reload(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def _health_check(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OnlineActionHandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        '_remote_execute': grpc.unary_unary_rpc_method_handler(
            servicer._remote_execute,
            request_deserializer=actions__pb2.OnlineActionRequest.FromString,
            response_serializer=actions__pb2.OnlineActionResponse.SerializeToString,
        ),
        '_remote_reload': grpc.unary_unary_rpc_method_handler(
            servicer._remote_reload,
            request_deserializer=actions__pb2.ReloadRequest.FromString,
            response_serializer=actions__pb2.ReloadResponse.SerializeToString,
        ),
        '_health_check': grpc.unary_unary_rpc_method_handler(
            servicer._health_check,
            request_deserializer=actions__pb2.HealthCheckRequest.FromString,
            response_serializer=actions__pb2.HealthCheckResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'OnlineActionHandler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


class BatchActionHandlerStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self._remote_execute = channel.unary_unary(
            '/BatchActionHandler/_remote_execute',
            request_serializer=actions__pb2.BatchActionRequest.SerializeToString,
            response_deserializer=actions__pb2.BatchActionResponse.FromString,
        )
        self._remote_reload = channel.unary_unary(
            '/BatchActionHandler/_remote_reload',
            request_serializer=actions__pb2.ReloadRequest.SerializeToString,
            response_deserializer=actions__pb2.ReloadResponse.FromString,
        )
        self._health_check = channel.unary_unary(
            '/BatchActionHandler/_health_check',
            request_serializer=actions__pb2.HealthCheckRequest.SerializeToString,
            response_deserializer=actions__pb2.HealthCheckResponse.FromString,
        )


class BatchActionHandlerServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def _remote_execute(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def _remote_reload(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def _health_check(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BatchActionHandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        '_remote_execute': grpc.unary_unary_rpc_method_handler(
            servicer._remote_execute,
            request_deserializer=actions__pb2.BatchActionRequest.FromString,
            response_serializer=actions__pb2.BatchActionResponse.SerializeToString,
        ),
        '_remote_reload': grpc.unary_unary_rpc_method_handler(
            servicer._remote_reload,
            request_deserializer=actions__pb2.ReloadRequest.FromString,
            response_serializer=actions__pb2.ReloadResponse.SerializeToString,
        ),
        '_health_check': grpc.unary_unary_rpc_method_handler(
            servicer._health_check,
            request_deserializer=actions__pb2.HealthCheckRequest.FromString,
            response_serializer=actions__pb2.HealthCheckResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'BatchActionHandler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
