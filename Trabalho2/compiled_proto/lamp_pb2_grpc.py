# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import lamp_pb2 as lamp__pb2


class LampStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.change_state = channel.unary_unary(
                '/Lamp/change_state',
                request_serializer=lamp__pb2.ChangeStateRequest.SerializeToString,
                response_deserializer=lamp__pb2.Response.FromString,
                )
        self.retrieve_state = channel.unary_unary(
                '/Lamp/retrieve_state',
                request_serializer=lamp__pb2.EmptyRequest.SerializeToString,
                response_deserializer=lamp__pb2.Response.FromString,
                )
        self.change_color = channel.unary_unary(
                '/Lamp/change_color',
                request_serializer=lamp__pb2.ColorRequest.SerializeToString,
                response_deserializer=lamp__pb2.Response.FromString,
                )


class LampServicer(object):
    """Missing associated documentation comment in .proto file."""

    def change_state(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def retrieve_state(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def change_color(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LampServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'change_state': grpc.unary_unary_rpc_method_handler(
                    servicer.change_state,
                    request_deserializer=lamp__pb2.ChangeStateRequest.FromString,
                    response_serializer=lamp__pb2.Response.SerializeToString,
            ),
            'retrieve_state': grpc.unary_unary_rpc_method_handler(
                    servicer.retrieve_state,
                    request_deserializer=lamp__pb2.EmptyRequest.FromString,
                    response_serializer=lamp__pb2.Response.SerializeToString,
            ),
            'change_color': grpc.unary_unary_rpc_method_handler(
                    servicer.change_color,
                    request_deserializer=lamp__pb2.ColorRequest.FromString,
                    response_serializer=lamp__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Lamp', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Lamp(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def change_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Lamp/change_state',
            lamp__pb2.ChangeStateRequest.SerializeToString,
            lamp__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def retrieve_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Lamp/retrieve_state',
            lamp__pb2.EmptyRequest.SerializeToString,
            lamp__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def change_color(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Lamp/change_color',
            lamp__pb2.ColorRequest.SerializeToString,
            lamp__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
