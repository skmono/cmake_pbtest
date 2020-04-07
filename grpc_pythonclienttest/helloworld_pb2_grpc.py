# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import helloworld_pb2 as helloworld__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/helloworld.Greeter/SayHello',
                request_serializer=helloworld__pb2.Request.SerializeToString,
                response_deserializer=helloworld__pb2.Reply.FromString,
                )
        self.SayBye = channel.unary_unary(
                '/helloworld.Greeter/SayBye',
                request_serializer=helloworld__pb2.Request.SerializeToString,
                response_deserializer=helloworld__pb2.Reply.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    """

    def SayHello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayBye(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=helloworld__pb2.Request.FromString,
                    response_serializer=helloworld__pb2.Reply.SerializeToString,
            ),
            'SayBye': grpc.unary_unary_rpc_method_handler(
                    servicer.SayBye,
                    request_deserializer=helloworld__pb2.Request.FromString,
                    response_serializer=helloworld__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/SayHello',
            helloworld__pb2.Request.SerializeToString,
            helloworld__pb2.Reply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayBye(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/SayBye',
            helloworld__pb2.Request.SerializeToString,
            helloworld__pb2.Reply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)