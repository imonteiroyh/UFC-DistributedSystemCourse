# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import humidifier_pb2 as proto_dot_humidifier__pb2


class HumidifierStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.change_smart_humidifier_state = channel.unary_unary(
                '/Humidifier/change_smart_humidifier_state',
                request_serializer=proto_dot_humidifier__pb2.ChangeSmartHumidifierRequest.SerializeToString,
                response_deserializer=proto_dot_humidifier__pb2.HumidifierResponse.FromString,
                )
        self.change_state = channel.unary_unary(
                '/Humidifier/change_state',
                request_serializer=proto_dot_humidifier__pb2.ChangeHumidifierStateRequest.SerializeToString,
                response_deserializer=proto_dot_humidifier__pb2.HumidifierResponse.FromString,
                )
        self.get_smart_humidifier_state = channel.unary_unary(
                '/Humidifier/get_smart_humidifier_state',
                request_serializer=proto_dot_humidifier__pb2.HumidifierEmptyRequest.SerializeToString,
                response_deserializer=proto_dot_humidifier__pb2.HumidifierResponse.FromString,
                )
        self.get_state = channel.unary_unary(
                '/Humidifier/get_state',
                request_serializer=proto_dot_humidifier__pb2.HumidifierEmptyRequest.SerializeToString,
                response_deserializer=proto_dot_humidifier__pb2.HumidifierResponse.FromString,
                )
        self.change_bounds = channel.unary_unary(
                '/Humidifier/change_bounds',
                request_serializer=proto_dot_humidifier__pb2.ChangeBoundsHumidifierRequest.SerializeToString,
                response_deserializer=proto_dot_humidifier__pb2.HumidifierResponse.FromString,
                )
        self.change_sensor_state = channel.unary_unary(
                '/Humidifier/change_sensor_state',
                request_serializer=proto_dot_humidifier__pb2.ChangeHumiditySensorStateRequest.SerializeToString,
                response_deserializer=proto_dot_humidifier__pb2.HumidifierResponse.FromString,
                )


class HumidifierServicer(object):
    """Missing associated documentation comment in .proto file."""

    def change_smart_humidifier_state(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def change_state(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_smart_humidifier_state(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_state(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def change_bounds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def change_sensor_state(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HumidifierServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'change_smart_humidifier_state': grpc.unary_unary_rpc_method_handler(
                    servicer.change_smart_humidifier_state,
                    request_deserializer=proto_dot_humidifier__pb2.ChangeSmartHumidifierRequest.FromString,
                    response_serializer=proto_dot_humidifier__pb2.HumidifierResponse.SerializeToString,
            ),
            'change_state': grpc.unary_unary_rpc_method_handler(
                    servicer.change_state,
                    request_deserializer=proto_dot_humidifier__pb2.ChangeHumidifierStateRequest.FromString,
                    response_serializer=proto_dot_humidifier__pb2.HumidifierResponse.SerializeToString,
            ),
            'get_smart_humidifier_state': grpc.unary_unary_rpc_method_handler(
                    servicer.get_smart_humidifier_state,
                    request_deserializer=proto_dot_humidifier__pb2.HumidifierEmptyRequest.FromString,
                    response_serializer=proto_dot_humidifier__pb2.HumidifierResponse.SerializeToString,
            ),
            'get_state': grpc.unary_unary_rpc_method_handler(
                    servicer.get_state,
                    request_deserializer=proto_dot_humidifier__pb2.HumidifierEmptyRequest.FromString,
                    response_serializer=proto_dot_humidifier__pb2.HumidifierResponse.SerializeToString,
            ),
            'change_bounds': grpc.unary_unary_rpc_method_handler(
                    servicer.change_bounds,
                    request_deserializer=proto_dot_humidifier__pb2.ChangeBoundsHumidifierRequest.FromString,
                    response_serializer=proto_dot_humidifier__pb2.HumidifierResponse.SerializeToString,
            ),
            'change_sensor_state': grpc.unary_unary_rpc_method_handler(
                    servicer.change_sensor_state,
                    request_deserializer=proto_dot_humidifier__pb2.ChangeHumiditySensorStateRequest.FromString,
                    response_serializer=proto_dot_humidifier__pb2.HumidifierResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Humidifier', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Humidifier(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def change_smart_humidifier_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Humidifier/change_smart_humidifier_state',
            proto_dot_humidifier__pb2.ChangeSmartHumidifierRequest.SerializeToString,
            proto_dot_humidifier__pb2.HumidifierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/Humidifier/change_state',
            proto_dot_humidifier__pb2.ChangeHumidifierStateRequest.SerializeToString,
            proto_dot_humidifier__pb2.HumidifierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_smart_humidifier_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Humidifier/get_smart_humidifier_state',
            proto_dot_humidifier__pb2.HumidifierEmptyRequest.SerializeToString,
            proto_dot_humidifier__pb2.HumidifierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Humidifier/get_state',
            proto_dot_humidifier__pb2.HumidifierEmptyRequest.SerializeToString,
            proto_dot_humidifier__pb2.HumidifierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def change_bounds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Humidifier/change_bounds',
            proto_dot_humidifier__pb2.ChangeBoundsHumidifierRequest.SerializeToString,
            proto_dot_humidifier__pb2.HumidifierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def change_sensor_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Humidifier/change_sensor_state',
            proto_dot_humidifier__pb2.ChangeHumiditySensorStateRequest.SerializeToString,
            proto_dot_humidifier__pb2.HumidifierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
