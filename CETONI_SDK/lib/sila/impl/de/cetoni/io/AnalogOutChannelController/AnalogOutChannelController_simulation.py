"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Analog Out Channel Controller*

:details: AnalogOutChannelController:
    Allows to control one analog out channel of an I/O module

:file:    AnalogOutChannelController_simulation.py
:authors: Florian Meinicke

:date: (creation)          2020-12-09T09:15:03.172511
:date: (last modification) 2020-12-09T09:15:03.172511

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
from .gRPC import AnalogOutChannelController_pb2 as AnalogOutChannelController_pb2
# from .gRPC import AnalogOutChannelController_pb2_grpc as AnalogOutChannelController_pb2_grpc

# import default arguments
from .AnalogOutChannelController_default_arguments import default_dict


# noinspection PyPep8Naming,PyUnusedLocal
class AnalogOutChannelControllerSimulation:
    """
    Implementation of the *Analog Out Channel Controller* in *Simulation* mode
        The SiLA 2 driver for Qmix I/O Devices
    """

    def __init__(self):
        """Class initialiser"""

        logging.debug('Started server in mode: {mode}'.format(mode='Simulation'))

    def _get_command_state(self, command_uuid: str) -> silaFW_pb2.ExecutionInfo:
        """
        Method to fill an ExecutionInfo message from the SiLA server for observable commands

        :param command_uuid: The uuid of the command for which to return the current state

        :return: An execution info object with the current command state
        """

        #: Enumeration of silaFW_pb2.ExecutionInfo.CommandStatus
        command_status = silaFW_pb2.ExecutionInfo.CommandStatus.waiting
        #: Real silaFW_pb2.Real(0...1)
        command_progress = None
        #: Duration silaFW_pb2.Duration(seconds=<seconds>, nanos=<nanos>)
        command_estimated_remaining = None
        #: Duration silaFW_pb2.Duration(seconds=<seconds>, nanos=<nanos>)
        command_lifetime_of_execution = None

        # TODO: check the state of the command with the given uuid and return the correct information

        # just return a default in this example
        return silaFW_pb2.ExecutionInfo(
            commandStatus=command_status,
            progressInfo=(
                command_progress if command_progress is not None else None
            ),
            estimatedRemainingTime=(
                command_estimated_remaining if command_estimated_remaining is not None else None
            ),
            updatedLifetimeOfExecution=(
                command_lifetime_of_execution if command_lifetime_of_execution is not None else None
            )
        )

    def SetOutputValue(self, request, context: grpc.ServicerContext) \
            -> AnalogOutChannelController_pb2.SetOutputValue_Responses:
        """
        Executes the unobservable command "Set Output Value"
            Set the value of the analog output channel.

        :param request: gRPC request containing the parameters passed:
            request.Value (Value): The value to set.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        # initialise the return value
        return_value = None

        # TODO:
        #   Add implementation of Simulation for command SetOutputValue here and write the resulting response
        #   in return_value

        # fallback to default
        if return_value is None:
            return_value = AnalogOutChannelController_pb2.SetOutputValue_Responses(
                **default_dict['SetOutputValue_Responses']
            )

        return return_value


    def Subscribe_Value(self, request, context: grpc.ServicerContext) \
            -> AnalogOutChannelController_pb2.Subscribe_Value_Responses:
        """
        Requests the observable property Value
            The value of the analog I/O channel.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.Value (Value): The value of the analog I/O channel.
        """

        # initialise the return value
        return_value: AnalogOutChannelController_pb2.Subscribe_Value_Responses = None

        # we could use a timeout here if we wanted
        while True:
            # TODO:
            #   Add implementation of Simulation for property Value here and write the resulting
            #   response in return_value

            # create the default value
            if return_value is None:
                return_value = AnalogOutChannelController_pb2.Subscribe_Value_Responses(
                    **default_dict['Subscribe_Value_Responses']
                )


            yield return_value

