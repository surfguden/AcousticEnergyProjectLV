"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Shutdown Controller*

:details: ShutdownController:
    Provides a generic way of telling a SiLA2 server that it is about to be shut down. The server implements a routine
    to be executed before the hardware is shut down (e.g. saving device paramters or bringing the device into a safe
    position).

:file:    ShutdownController_real.py
:authors: Florian Meinicke

:date: (creation)          2019-07-17T09:54:01.898782
:date: (last modification) 2019-10-05T11:53:30.865733

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
import os
import logging
import time         # used for observables
import uuid         # used for observables
import grpc         # used for type hinting only

from configparser import ConfigParser

from typing import Union

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2
from sila2lib._internal.config import get_config_dir as sila_get_config_dir

# import gRPC modules for this feature
from .gRPC import ShutdownController_pb2 as ShutdownController_pb2
# from .gRPC import ShutdownController_pb2_grpc as ShutdownController_pb2_grpc

# import SiLA errors
from impl.common.qmix_errors import SiLAFrameworkError, SiLAFrameworkErrorType

# import default arguments
from .ShutdownController_default_arguments import default_dict

# import qmixsdk
from qmixsdk.qmixpump import Pump, ContiFlowPump, ContiFlowProperty
from qmixsdk.qmixmotion import Axis, AxisSystem

# noinspection PyPep8Naming,PyUnusedLocal
class ShutdownControllerReal:
    """
    Implementation of the *Shutdown Controller* in *Real* mode
        This is a sample service for controlling neMESYS syringe pumps via SiLA2
    """

    def __init__(self, device: Union[Pump, AxisSystem], server_name, sila2_conf: ConfigParser):
        """Class initialiser"""

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

        self.device = device
        self.server_name = server_name
        self.sila2_config = sila2_conf

        self.command_uuid = ""

    def _save_contiflow_params(self):
        """
        Saves the current contiflow parameters so that they can be restored the next time.
        """
        pump_name = self.device.get_pump_name()
        self.sila2_config[pump_name] = {}
        self.sila2_config[pump_name]["crossflow_duration"] = \
            str(self.device.get_device_property(ContiFlowProperty.CROSSFLOW_DURATION_S))
        self.sila2_config[pump_name]["overlap_duration"] = \
            str(self.device.get_device_property(ContiFlowProperty.OVERLAP_DURATION_S))
        self.sila2_config[pump_name]["refill_flow"] = \
            str(self.device.get_device_property(ContiFlowProperty.REFILL_FLOW))
        self.sila2_config[pump_name]["switching_mode"] = \
            str(self.device.get_device_property(ContiFlowProperty.SWITCHING_MODE))
        logging.debug("Saving contiflow parameters for %s", pump_name)

    def _save_drive_position_counters(self, device: Union[Pump, AxisSystem]):
        """
        Saves the current drive position counters of the given `device` so that they can be restored next time.

        :param device: The device for which to save the position counters
        """
        if isinstance(device, Pump):
            pump_name = device.get_pump_name()
            drive_pos_counter = device.get_position_counter_value()
            self.sila2_config[pump_name] = {}
            self.sila2_config[pump_name]["drive_pos_counter"] = str(drive_pos_counter)
            logging.debug("Saving drive position counter (%d) for %s",
                        drive_pos_counter, pump_name)
        elif isinstance(device, AxisSystem):
            for i in range(device.get_axes_count()):
                axis = device.get_axis_device(i)
                axis_name = axis.get_device_name()
                drive_pos_counter = axis.get_position_counter()
                self.sila2_config[axis_name] = {}
                self.sila2_config[axis_name]["drive_pos_counter"] = str(drive_pos_counter)
                logging.debug("Saving drive position counter (%d) for %s",
                            drive_pos_counter, axis_name)

    def _write_config(self):
        """
        Writes the current config to the config file
        """
        config_dir = sila_get_config_dir(subdir=self.server_name)
        config_filename = os.path.join(config_dir, self.server_name + '.conf')

        logging.debug("Saving config to file %s", config_filename)
        with open(config_filename, "w") as config_file:
            self.sila2_config.write(config_file)


    def Shutdown(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Shutdown"
            Initiates the shutdown routine. If no errors occured during the shutdown process the server should be considered ready to be physically shutdown (i.e. the device can be shut down/powered off).

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        # respond with UUID
        self.command_uuid = str(uuid.uuid4())

        if isinstance(self.device, ContiFlowPump):
            self._save_contiflow_params()
            for i in range(2):
                self._save_drive_position_counters(self.device.get_syringe_pump(i))
        else:
            self._save_drive_position_counters(self.device)

        self._write_config()

        return silaFW_pb2.CommandConfirmation(
            commandExecutionUUID=silaFW_pb2.CommandExecutionUUID(value=self.command_uuid)
        )

    def Shutdown_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.Shutdown`.

        :param request: A request object with the following properties
            commandId: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """
        # Get the UUID of the command
        command_uuid = request.value

        if not command_uuid or command_uuid != self.command_uuid:
            raise SiLAFrameworkError(
                error_type=SiLAFrameworkErrorType.INVALID_COMMAND_EXECUTION_UUID
            )

        yield silaFW_pb2.ExecutionInfo(
            commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.running
        )
        yield silaFW_pb2.ExecutionInfo(
            commandStatus=silaFW_pb2.ExecutionInfo.CommandStatus.finishedSuccessfully
        )

    def Shutdown_Result(self, request, context: grpc.ServicerContext) \
            -> ShutdownController_pb2.Shutdown_Responses:
        """
        Returns the final result of the command call :meth:`~.Shutdown`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        return ShutdownController_pb2.Shutdown_Responses()
