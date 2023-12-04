"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Digital Out Channel Controller*

:details: DigitalOutChannelController:
    Allows to control one digital out channel of an I/O module

:file:    DigitalOutChannelController_real.py
:authors: Florian Meinicke

:date: (creation)          2020-12-08T14:25:47.312796
:date: (last modification) 2020-12-08T14:25:47.312796

.. note:: Code generated by sila2codegenerator 0.2.0

________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""

__version__ = "0.1.0"

# import general packages
import logging
import time         # used for observables
import uuid         # used for observables
import grpc         # used for type hinting only

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2

# import gRPC modules for this feature
from .gRPC import DigitalOutChannelController_pb2 as DigitalOutChannelController_pb2
# from .gRPC import DigitalOutChannelController_pb2_grpc as DigitalOutChannelController_pb2_grpc

# import default arguments
from .DigitalOutChannelController_default_arguments import default_dict

# import channel gateway feature
from impl.de.cetoni.core.ChannelGatewayService import ChannelGatewayService_servicer as ChannelGatewayService

# noinspection PyPep8Naming,PyUnusedLocal
class DigitalOutChannelControllerReal:
    """
    Implementation of the *Digital Out Channel Controller* in *Real* mode
        The SiLA 2 driver for Qmix I/O Devices
    """

    def __init__(self, channel_gateway: ChannelGatewayService):
        """
        Class initialiser

        :param channel_gateway: The ChannelGatewayService feature that provides
                                the channels that this feature can operate on
        """

        self.channel_gateway = channel_gateway
        self.states = {True: 'On', False: 'Off'}

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

    def SetOutput(self, request, context: grpc.ServicerContext) \
            -> DigitalOutChannelController_pb2.SetOutput_Responses:
        """
        Executes the unobservable command "Set Output"
            Switch a digital output channel on or off.

        :param request: gRPC request containing the parameters passed:
            request.State (State): The state to set.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        state = request.State.State.value
        logging.info(f"Setting output state to {state}")
        self.channel_gateway.get_channel(context.invocation_metadata(), "Command").write_on(state == 'On')

        return DigitalOutChannelController_pb2.SetOutput_Responses()


    def Subscribe_State(self, request, context: grpc.ServicerContext) \
            -> DigitalOutChannelController_pb2.Subscribe_State_Responses:
        """
        Requests the observable property State
            The state of the channel.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.State (State): The state of the channel.
        """

        channel = self.channel_gateway.get_channel(context.invocation_metadata(), "Property")

        while True:
            yield DigitalOutChannelController_pb2.Subscribe_State_Responses(
                State=DigitalOutChannelController_pb2.DataType_State(
                    State=silaFW_pb2.String(value=self.states[channel.is_output_on()])
                )
            )
            time.sleep(0.5) # give client some time to catch up

