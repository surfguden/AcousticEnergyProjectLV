# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import AxisSystemPositionController_pb2 as AxisSystemPositionController__pb2
import sila2lib.framework.SiLAFramework_pb2 as SiLAFramework__pb2


class AxisSystemPositionControllerStub(object):
    """Feature: Axis System Position Controller
    Allows to control the position of an axis system
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MoveToPosition = channel.unary_unary(
                '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/MoveToPosition',
                request_serializer=AxisSystemPositionController__pb2.MoveToPosition_Parameters.SerializeToString,
                response_deserializer=SiLAFramework__pb2.CommandConfirmation.FromString,
                )
        self.MoveToPosition_Info = channel.unary_stream(
                '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/MoveToPosition_Info',
                request_serializer=SiLAFramework__pb2.CommandExecutionUUID.SerializeToString,
                response_deserializer=SiLAFramework__pb2.ExecutionInfo.FromString,
                )
        self.MoveToPosition_Result = channel.unary_unary(
                '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/MoveToPosition_Result',
                request_serializer=SiLAFramework__pb2.CommandExecutionUUID.SerializeToString,
                response_deserializer=AxisSystemPositionController__pb2.MoveToPosition_Responses.FromString,
                )
        self.MoveToHomePosition = channel.unary_unary(
                '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/MoveToHomePosition',
                request_serializer=AxisSystemPositionController__pb2.MoveToHomePosition_Parameters.SerializeToString,
                response_deserializer=AxisSystemPositionController__pb2.MoveToHomePosition_Responses.FromString,
                )
        self.StopMoving = channel.unary_unary(
                '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/StopMoving',
                request_serializer=AxisSystemPositionController__pb2.StopMoving_Parameters.SerializeToString,
                response_deserializer=AxisSystemPositionController__pb2.StopMoving_Responses.FromString,
                )
        self.Subscribe_Position = channel.unary_stream(
                '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/Subscribe_Position',
                request_serializer=AxisSystemPositionController__pb2.Subscribe_Position_Parameters.SerializeToString,
                response_deserializer=AxisSystemPositionController__pb2.Subscribe_Position_Responses.FromString,
                )


class AxisSystemPositionControllerServicer(object):
    """Feature: Axis System Position Controller
    Allows to control the position of an axis system
    """

    def MoveToPosition(self, request, context):
        """Move To Position
        Move the axis system to the given position with a certain velocity
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveToPosition_Info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveToPosition_Result(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveToHomePosition(self, request, context):
        """Move To Home Position
        Move the axis system to its home position. The axis system should manage the order of the movement and should know how
        to move all axes into a home state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopMoving(self, request, context):
        """Stop Moving
        Immediately stops all movement of the axis system
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe_Position(self, request, context):
        """Position
        The current XY position of the axis system
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AxisSystemPositionControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MoveToPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveToPosition,
                    request_deserializer=AxisSystemPositionController__pb2.MoveToPosition_Parameters.FromString,
                    response_serializer=SiLAFramework__pb2.CommandConfirmation.SerializeToString,
            ),
            'MoveToPosition_Info': grpc.unary_stream_rpc_method_handler(
                    servicer.MoveToPosition_Info,
                    request_deserializer=SiLAFramework__pb2.CommandExecutionUUID.FromString,
                    response_serializer=SiLAFramework__pb2.ExecutionInfo.SerializeToString,
            ),
            'MoveToPosition_Result': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveToPosition_Result,
                    request_deserializer=SiLAFramework__pb2.CommandExecutionUUID.FromString,
                    response_serializer=AxisSystemPositionController__pb2.MoveToPosition_Responses.SerializeToString,
            ),
            'MoveToHomePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveToHomePosition,
                    request_deserializer=AxisSystemPositionController__pb2.MoveToHomePosition_Parameters.FromString,
                    response_serializer=AxisSystemPositionController__pb2.MoveToHomePosition_Responses.SerializeToString,
            ),
            'StopMoving': grpc.unary_unary_rpc_method_handler(
                    servicer.StopMoving,
                    request_deserializer=AxisSystemPositionController__pb2.StopMoving_Parameters.FromString,
                    response_serializer=AxisSystemPositionController__pb2.StopMoving_Responses.SerializeToString,
            ),
            'Subscribe_Position': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe_Position,
                    request_deserializer=AxisSystemPositionController__pb2.Subscribe_Position_Parameters.FromString,
                    response_serializer=AxisSystemPositionController__pb2.Subscribe_Position_Responses.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AxisSystemPositionController(object):
    """Feature: Axis System Position Controller
    Allows to control the position of an axis system
    """

    @staticmethod
    def MoveToPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/MoveToPosition',
            AxisSystemPositionController__pb2.MoveToPosition_Parameters.SerializeToString,
            SiLAFramework__pb2.CommandConfirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveToPosition_Info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/MoveToPosition_Info',
            SiLAFramework__pb2.CommandExecutionUUID.SerializeToString,
            SiLAFramework__pb2.ExecutionInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveToPosition_Result(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/MoveToPosition_Result',
            SiLAFramework__pb2.CommandExecutionUUID.SerializeToString,
            AxisSystemPositionController__pb2.MoveToPosition_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveToHomePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/MoveToHomePosition',
            AxisSystemPositionController__pb2.MoveToHomePosition_Parameters.SerializeToString,
            AxisSystemPositionController__pb2.MoveToHomePosition_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopMoving(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/StopMoving',
            AxisSystemPositionController__pb2.StopMoving_Parameters.SerializeToString,
            AxisSystemPositionController__pb2.StopMoving_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe_Position(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController/Subscribe_Position',
            AxisSystemPositionController__pb2.Subscribe_Position_Parameters.SerializeToString,
            AxisSystemPositionController__pb2.Subscribe_Position_Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
