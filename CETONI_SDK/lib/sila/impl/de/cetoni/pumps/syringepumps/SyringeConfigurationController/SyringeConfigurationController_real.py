"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Syringe Configuration Controller*

:details: SyringeConfigurationController:
    Provides syringe pump specific functions for configuration (i.e. the configuration of the syringe itself).

:file:    SyringeConfigurationController_real.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.313557
:date: (last modification) 2019-10-05T11:53:30.852642

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

# import SiLA errors
from impl.common.qmix_errors import SiLAValidationError

# import default arguments
from .SyringeConfigurationController_default_arguments import default_dict

# import qmixsdk
from qmixsdk import qmixpump

# noinspection PyPep8Naming,PyUnusedLocal
class SyringeConfigurationControllerReal:
    """
    Implementation of the *Syringe Configuration Controller* in *Real* mode
        This is a sample service for controlling neMESYS syringe pumps via SiLA2
    """

    def __init__(self, pump: qmixpump.Pump):
        """Class initialiser"""

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

        self.pump = pump

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

        def check_less_than_zero(param, param_str: str):
            """
            Checks if the given param is less than zero. If this is the case,
            an appropriate validation error is raised indicating to the client
            which parameter should be adjusted.

                :param param: The parameter to check against zero
                :param param_str: A string description of the given param
            """
            if param < 0:
                raise SiLAValidationError(
                    parameter=param_str,
                    msg=f"The {param_str} cannot be less than 0",
                )

        requested_inner_diameter = request.InnerDiameter.value
        check_less_than_zero(requested_inner_diameter, "InnerDiameter")
        requested_piston_stroke = request.MaxPistonStroke.value
        check_less_than_zero(requested_piston_stroke, "MaxPistonStroke")

        self.pump.set_syringe_param(requested_inner_diameter, requested_piston_stroke)

        return SyringeConfigurationController_pb2.SetSyringeParameters_Responses()

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

        while True:
            yield SyringeConfigurationController_pb2.Subscribe_InnerDiameter_Responses(
                InnerDiameter=silaFW_pb2.Real(value=self.pump.get_syringe_param().inner_diameter_mm)
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)


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

        while True:
            yield SyringeConfigurationController_pb2.Subscribe_MaxPistonStroke_Responses(
                MaxPistonStroke=silaFW_pb2.Real(
                    value=self.pump.get_syringe_param().max_piston_stroke_mm
                )
            )

            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)

