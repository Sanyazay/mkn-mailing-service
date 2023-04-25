# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mail_service_pb2 as mail__service__pb2


class MailingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ScheduleNotification = channel.unary_unary(
                '/MailingService/ScheduleNotification',
                request_serializer=mail__service__pb2.ScheduleRequest.SerializeToString,
                response_deserializer=mail__service__pb2.ScheduleResponse.FromString,
                )


class MailingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ScheduleNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MailingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ScheduleNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.ScheduleNotification,
                    request_deserializer=mail__service__pb2.ScheduleRequest.FromString,
                    response_serializer=mail__service__pb2.ScheduleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MailingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MailingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ScheduleNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MailingService/ScheduleNotification',
            mail__service__pb2.ScheduleRequest.SerializeToString,
            mail__service__pb2.ScheduleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)