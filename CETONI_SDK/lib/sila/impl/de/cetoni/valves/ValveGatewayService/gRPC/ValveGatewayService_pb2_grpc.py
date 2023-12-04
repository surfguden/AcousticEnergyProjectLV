# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import ValveGatewayService_pb2 as ValveGatewayService__pb2


class ValveGatewayServiceStub(object):
    """Feature: Valve Gateway Service
    Provides means to access individual valves of a valve terminal
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get_ValveIdentifiers = channel.unary_unary(
                '/sila2.de.cetoni.valves.valvegatewayservice.v1.ValveGatewayService/Get_ValveIdentifiers',
                request_serializer=ValveGatewayService__pb2.Get_ValveIdentifiers_Parameters.SerializeToString,
                response_deserializer=ValveGatewayService__pb2.Get_ValveIdentifiers_Responses.FromString,
                )
        self.Get_FCPAffectedByMetadata_ValveIdentifier = channel.unary_unary(
                '/sila2.de.cetoni.valves.valvegatewayservice.v1.ValveGatewayService/Get_FCPAffectedByMetadata_ValveIdentifier',
                request_serializer=ValveGatewayService__pb2.Get_FCPAffectedByMetadata_ValveIdentifier_Parameters.SerializeToString,
                response_deserializer=ValveGatewayService__pb2.Get_FCPAffectedByMetadata_ValveIdentifier_Responses.FromString,
                )


class ValveGatewayServiceServicer(object):
    """Feature: Valve Gateway Service
    Provides means to access individual valves of a valve terminal
    """

    def Get_ValveIdentifiers(self, request, context):
        """Valve Identifiers
        A list of all possible valve names (identifiers) of this device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get_FCPAffectedByMetadata_ValveIdentifier(self, request, context):
        """Valve Identifier
        The identifier of a single valve of a valve terminal
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ValveGatewayServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get_ValveIdentifiers': grpc.unary_unary_rpc_method_handler(
                    servicer.Get_ValveIdentifiers,
                    request_deserializer=ValveGatewayService__pb2.Get_ValveIdentifiers_Parameters.FromString,
                    response_serializer=ValveGatewayService__pb2.Get_ValveIdentifiers_Responses.SerializeToString,
            ),
            'Get_FCPAffectedByMetadata_ValveIdentifier': grpc.unary_unary_rpc_method_handler(
                    servicer.Get_FCPAffectedByMetadata_ValveIdentifier,
                    request_deserializer=ValveGatewayService__pb2.Get_FCPAffectedByMetadata_ValveIdentifier_Parameters.FromString,
                    response_serializer=ValveGatewayService__pb2.Get_FCPAffectedByMetadata_ValveIdentifier_Responses.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sila2.de.cetoni.valves.valvegatewayservice.v1.ValveGatewayService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ValveGatewayService(object):
    """Feature: Valve Gateway Service
    Provides means to access individual valves of a valve terminal
    """

    @staticmethod
    def Get_ValveIdentifiers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.valves.valvegatewayservice.v1.ValveGatewayService/Get_ValveIdentifiers',
            ValveGatewayService__pb2.Get_ValveIdentifiers_Parameters.SerializeToString,
            ValveGatewayService__pb2.Get_ValveIdentifiers_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get_FCPAffectedByMetadata_ValveIdentifier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.valves.valvegatewayservice.v1.ValveGatewayService/Get_FCPAffectedByMetadata_ValveIdentifier',
            ValveGatewayService__pb2.Get_FCPAffectedByMetadata_ValveIdentifier_Parameters.SerializeToString,
            ValveGatewayService__pb2.Get_FCPAffectedByMetadata_ValveIdentifier_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
