"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Syringe Configuration Controller*

:details: SyringeConfigurationController:
    Provides syringe pump specific functions for configuration (i.e. the configuration of the syringe itself).

:file:    SyringeConfigurationController_servicer.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.309829
:date: (last modification) 2019-10-05T11:53:30.847400

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
import grpc

# meta packages
from typing import Union

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2
# import SiLA errors
from impl.common.qmix_errors import SiLAValidationError, DeviceError, QmixSDKSiLAError

# import gRPC modules for this feature
from .gRPC import SyringeConfigurationController_pb2 as SyringeConfigurationController_pb2
from .gRPC import SyringeConfigurationController_pb2_grpc as SyringeConfigurationController_pb2_grpc

# import simulation and real implementation
from .SyringeConfigurationController_simulation import SyringeConfigurationControllerSimulation
from .SyringeConfigurationController_real import SyringeConfigurationControllerReal


class SyringeConfigurationController(SyringeConfigurationController_pb2_grpc.SyringeConfigurationControllerServicer):
    """
    This is a sample service for controlling neMESYS syringe pumps via SiLA2
    """
    implementation: Union[SyringeConfigurationControllerSimulation, SyringeConfigurationControllerReal]
    simulation_mode: bool

    def __init__(self, pump, simulation_mode: bool = True):
        """
        Class initialiser.

        :param pump: A valid `qxmixpump` for this service to use
        :param simulation_mode: Sets whether at initialisation the simulation mode is active or the real mode
        """

        self.pump = pump

        self.simulation_mode = simulation_mode
        if simulation_mode:
            self.switch_to_simulation_mode()
        else:
            self.switch_to_real_mode()

    def _inject_implementation(self,
                               implementation: Union[SyringeConfigurationControllerSimulation,
                                                     SyringeConfigurationControllerReal]
                               ) -> bool:
        """
        Dependency injection of the implementation used.
            Allows to set the class used for simulation/real mode.

        :param implementation: A valid implementation of the neMESYSServicer.
        """

        self.implementation = implementation
        return True

    def switch_to_simulation_mode(self):
        """Method that will automatically be called by the server when the simulation mode is requested."""
        self.simulation_mode = True
        self._inject_implementation(SyringeConfigurationControllerSimulation())

    def switch_to_real_mode(self):
        """Method that will automatically be called by the server when the real mode is requested."""
        self.simulation_mode = False
        self._inject_implementation(SyringeConfigurationControllerReal(self.pump))

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

        logging.debug(
            "SetSyringeParameters called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.SetSyringeParameters(request, context)
        except (DeviceError, SiLAValidationError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)

    def Subscribe_InnerDiameter(self, request, context: grpc.ServicerContext) \
            -> SyringeConfigurationController_pb2.Subscribe_InnerDiameter_Responses:
        """
        Requests the observable property Inner Diameter
            Inner diameter of the syringe tube in millimetres.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.InnerDiameter (Inner Diameter): Inner diameter of the syringe tube in millimetres.
        """

        logging.debug(
            "Property InnerDiameter requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            for value in self.implementation.Subscribe_InnerDiameter(request, context):
                yield value
        except DeviceError as err:
            err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)


    def Subscribe_MaxPistonStroke(self, request, context: grpc.ServicerContext) \
            -> SyringeConfigurationController_pb2.Subscribe_MaxPistonStroke_Responses:
        """
        Requests the observable property Max Piston Stroke
            The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.MaxPistonStroke (Max Piston Stroke): The maximum piston stroke defines the maximum position the piston can be moved to before it slips out of the syringe tube. The maximum piston stroke limits the maximum travel range of the syringe pump pusher.
        """

        logging.debug(
            "Property MaxPistonStroke requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            for value in self.implementation.Subscribe_MaxPistonStroke(request, context):
                yield value
        except DeviceError as err:
            err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)

