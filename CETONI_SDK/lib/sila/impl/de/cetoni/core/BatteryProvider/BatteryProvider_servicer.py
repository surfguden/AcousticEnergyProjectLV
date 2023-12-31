"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Battery Provider*

:details: BatteryProvider:
    Provides information on the battery state

:file:    BatteryProvider_servicer.py
:authors: Florian Meinicke

:date: (creation)          2021-04-20T06:40:34.351081
:date: (last modification) 2021-04-20T06:40:34.351081

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
import grpc

# meta packages
from typing import Union

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2
from sila2lib.error_handling.server_err import SiLAError, SiLAValidationError

# import gRPC modules for this feature
from .gRPC import BatteryProvider_pb2 as BatteryProvider_pb2
from .gRPC import BatteryProvider_pb2_grpc as BatteryProvider_pb2_grpc

# import simulation and real implementation
from .BatteryProvider_simulation import BatteryProviderSimulation
from .BatteryProvider_real import BatteryProviderReal



class BatteryProvider(BatteryProvider_pb2_grpc.BatteryProviderServicer):
    """
    The SiLA 2 driver for Qmix Control Devices
    """
    implementation: Union[BatteryProviderSimulation, BatteryProviderReal]
    simulation_mode: bool

    def __init__(self, simulation_mode: bool = True):
        """
        Class initialiser.

        :param simulation_mode: Sets whether at initialisation the simulation mode is active or the real mode.
        :param hardware_interface (optional): access to shared hardware interface, like serial interface.
        """

        self.simulation_mode = simulation_mode
        if simulation_mode:
            self._inject_implementation(BatteryProviderSimulation())
        else:
            self._inject_implementation(BatteryProviderReal())

    def _inject_implementation(self,
                               implementation: Union[BatteryProviderSimulation,
                                                     BatteryProviderReal]
                               ) -> bool:
        """
        Dependency injection of the implementation used.
            Allows to set the class used for simulation/real mode.

        :param implementation: A valid implementation of the QmixControlServicer.
        """

        self.implementation = implementation
        return True

    def switch_to_simulation_mode(self):
        """Method that will automatically be called by the server when the simulation mode is requested."""
        self.simulation_mode = True
        self._inject_implementation(BatteryProviderSimulation())

    def switch_to_real_mode(self):
        """Method that will automatically be called by the server when the real mode is requested."""
        self.simulation_mode = False
        self._inject_implementation(BatteryProviderReal())



    def Subscribe_BatteryVoltage(self, request, context: grpc.ServicerContext) \
            -> BatteryProvider_pb2.Subscribe_BatteryVoltage_Responses:
        """
        Requests the observable property Battery Voltage
            The current voltage of the battery

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.BatteryVoltage (Battery Voltage): The current voltage of the battery
        """

        logging.debug(
            "Property BatteryVoltage requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        try:
            return self.implementation.Subscribe_BatteryVoltage(request, context)
        except SiLAError as err:
            err.raise_rpc_error(context=context)

