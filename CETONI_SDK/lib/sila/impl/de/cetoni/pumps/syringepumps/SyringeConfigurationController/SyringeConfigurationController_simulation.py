"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Syringe Configuration Controller*

:details: SyringeConfigurationController:
    Provides syringe pump specific functions for configuration (i.e. the configuration of the syringe itself).

:file:    SyringeConfigurationController_simulation.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.311861
:date: (last modification) 2019-10-05T11:53:30.849787

.. note:: Code generated by SiLA2CodeGenerator 0.2.0

________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""

__version__ = "0.0.1"

# import general packages
import logging
import time         # used for observables
import uuid         # used for observables
import grpc         # used for type hinting only

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2

# import gRPC modules for this feature
from .gRPC import SyringeConfigurationController_pb2 as SyringeConfigurationController_pb2
# from .gRPC import SyringeConfigurationController_pb2_grpc as SyringeConfigurationController_pb2_grpc

# import default arguments
from .SyringeConfigurationController_default_arguments import default_dict


# noinspection PyPep8Naming,PyUnusedLocal
class SyringeConfigurationControllerSimulation:
    """
    Implementation of the *Syringe Configuration Controller* in *Simulation* mode
        This is a sample service for controlling neMESYS syringe pumps via SiLA2
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

    def SetSyringeParameters(self, request, context: grpc.ServicerContext) \
            -> SyringeConfigurationController_pb2.SetSyringeParameters_Responses:
        """
        Executes the unobservable command "Set Syringe Parameters"
            Set syringe parameters.
            If you change the syringe in one device, you need to setup the new syringe parameters to get proper conversion of flow rate und volume units.

        :param request: gRPC request containing the parameters passed:
            request.InnerDiameter (Inner Diameter): Inner diameter of the syringe tube in millimetres.
            request.MaxPistonStroke (Max Piston Stroke): The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        # initialise the return value
        return_value = None

        # TODO:
        #   Add implementation of Simulation for command SetSyringeParameters here and write the resulting response
        #   in return_value

        # fallback to default
        if return_value is None:
            return_value = SyringeConfigurationController_pb2.SetSyringeParameters_Responses(
                **default_dict['SetSyringeParameters_Responses']
            )

        return return_value


    def Subscribe_InnerDiameter(self, request, context: grpc.ServicerContext) \
            -> SyringeConfigurationController_pb2.Subscribe_InnerDiameter_Responses:
        """
        Requests the observable property Inner Diameter
            Inner diameter of the syringe tube in millimetres.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.InnerDiameter (Inner Diameter): Inner diameter of the syringe tube in millimetres.
        """

        # initialise the return value
        return_value: SyringeConfigurationController_pb2.Subscribe_InnerDiameter_Responses = None

        # we could use a timeout here if we wanted
        while True:
            # TODO:
            #   Add implementation of Simulation for property InnerDiameter here and write the resulting
            #   response in return_value

            # create the default value
            if return_value is None:
                return_value = SyringeConfigurationController_pb2.Subscribe_InnerDiameter_Responses(
                    **default_dict['Subscribe_InnerDiameter_Responses']
                )


            yield return_value


    def Subscribe_MaxPistonStroke(self, request, context: grpc.ServicerContext) \
            -> SyringeConfigurationController_pb2.Subscribe_MaxPistonStroke_Responses:
        """
        Requests the observable property Max Piston Stroke
            The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.MaxPistonStroke (Max Piston Stroke): The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.
        """

        # initialise the return value
        return_value: SyringeConfigurationController_pb2.Subscribe_MaxPistonStroke_Responses = None

        # we could use a timeout here if we wanted
        while True:
            # TODO:
            #   Add implementation of Simulation for property MaxPistonStroke here and write the resulting
            #   response in return_value

            # create the default value
            if return_value is None:
                return_value = SyringeConfigurationController_pb2.Subscribe_MaxPistonStroke_Responses(
                    **default_dict['Subscribe_MaxPistonStroke_Responses']
                )


            yield return_value
