"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Battery Provider*

:details: BatteryProvider:
    Provides information on the battery state

:file:    BatteryProvider_simulation.py
:authors: Florian Meinicke

:date: (creation)          2021-04-20T06:40:36.172052
:date: (last modification) 2021-04-20T06:40:36.172052

.. note:: Code generated by sila2codegenerator 0.3.6

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
from .gRPC import BatteryProvider_pb2 as BatteryProvider_pb2
# from .gRPC import BatteryProvider_pb2_grpc as BatteryProvider_pb2_grpc

# import default arguments
from .BatteryProvider_default_arguments import default_dict



# noinspection PyPep8Naming,PyUnusedLocal
class BatteryProviderSimulation:
    """
    Implementation of the *Battery Provider* in *Simulation* mode
        The SiLA 2 driver for Qmix Control Devices
    """

    def __init__(self, hardware_interface=None):
        """Class initialiser"""

        self.hardware_interface = hardware_interface

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



    def Subscribe_BatteryVoltage(self, request, context: grpc.ServicerContext) \
            -> BatteryProvider_pb2.Subscribe_BatteryVoltage_Responses:
        """
        Requests the observable property Battery Voltage
            The current voltage of the battery

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.BatteryVoltage (Battery Voltage): The current voltage of the battery
        """

        # initialise the return value
        return_value: BatteryProvider_pb2.Subscribe_BatteryVoltage_Responses = None

        # we could use a timeout here if we wanted
        while True:
            # TODO:
            #   Add implementation of Simulation for property BatteryVoltage here and write the resulting
            #   response in return_value

            # create the default value
            if return_value is None:
                return_value = BatteryProvider_pb2.Subscribe_BatteryVoltage_Responses(
                    #**default_dict['Subscribe_BatteryVoltage_Responses']
                BatteryVoltage=silaFW_pb2.Real(value=1.0)
                )


            yield return_value

