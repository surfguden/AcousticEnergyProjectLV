"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Pump Unit Controller*

:details: PumpUnitController:
    Allows to control the currently used units for passing and retrieving flow rates and volumes to and from a pump.

:file:    PumpUnitController_real.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.291719
:date: (last modification) 2019-10-05T11:53:30.822915

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

# import qmixsdk
from qmixsdk import qmixpump

from . import unit_conversion as uc

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2
# import SiLA errors
from impl.common.qmix_errors import UnitConversionError

# import gRPC modules for this feature
from .gRPC import PumpUnitController_pb2 as PumpUnitController_pb2
# from .gRPC import PumpUnitController_pb2_grpc as PumpUnitController_pb2_grpc

# import default arguments
from .PumpUnitController_default_arguments import default_dict


# noinspection PyPep8Naming,PyUnusedLocal
class PumpUnitControllerReal:
    """
    Implementation of the *Pump Unit Controller* in *Real* mode
        This is a sample service for controlling neMESYS syringe pumps via SiLA2
    """

    def __init__(self, pump: qmixpump.Pump):
        """Class initialiser"""

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

        self.pump = pump

    def SetFlowUnit(self, request, context: grpc.ServicerContext) \
            -> PumpUnitController_pb2.SetFlowUnit_Responses:
        """
        Executes the unobservable command "Set Flow Unit"
            Sets the flow unit for the pump. The flow unit defines the unit to be used for all flow values passed to or retrieved from the pump.

        :param request: gRPC request containing the parameters passed:
            request.FlowUnit (Flow Unit): The flow unit to be set.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        """
        FlowUnit {
            VolumeUnit {
                VolumeUnit {
                    value: "l"
                }
            }
            TimeUnit {
                TimeUnit {
                    value: "h"
                }
            }
        }
        """
        try:
            flow_unit = request.FlowUnit
            requested_volume_unit = flow_unit.VolumeUnit.VolumeUnit.value
            requested_time_unit = flow_unit.TimeUnit.TimeUnit.value
            prefix, volume_unit, time_unit = uc.evaluate_units(requested_volume_unit,
                                                               requested_time_unit)
        except ValueError:
            raise UnitConversionError(
                parameter="FlowUnit",
                msg="The given flow unit is malformed. It has to be something like 'ml/s', for instance."
            )
        else:
            self.pump.set_flow_unit(prefix, volume_unit, time_unit)
        return PumpUnitController_pb2.SetFlowUnit_Responses()


    def SetVolumeUnit(self, request, context: grpc.ServicerContext) \
            -> PumpUnitController_pb2.SetVolumeUnit_Responses:
        """
        Executes the unobservable command "Set Volume Unit"
            Sets the default volume unit. The volume unit defines the unit to be used for all volume values passed to or retrieved from the pump.

        :param request: gRPC request containing the parameters passed:
            request.VolumeUnit (Volume Unit): The volume unit for the flow rate.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        """
        VolumeUnit {
            VolumeUnit {
                value: "ml"
            }
        }
        """

        prefix, volume_unit = uc.evaluate_units(request.VolumeUnit.VolumeUnit.value)
        self.pump.set_volume_unit(prefix, volume_unit)

        return PumpUnitController_pb2.SetVolumeUnit_Responses()

    def Subscribe_FlowUnit(self, request, context: grpc.ServicerContext) \
            -> PumpUnitController_pb2.Subscribe_FlowUnit_Responses:
        """
        Requests the observable property Flow Unit
            The currently used flow unit.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.FlowUnit (Flow Unit): The currently used flow unit.
        """

        while True:
            volume_unit, time_unit = uc.flow_unit_to_string(self.pump.get_flow_unit()).split('/')
            yield PumpUnitController_pb2.Subscribe_FlowUnit_Responses(
                FlowUnit=PumpUnitController_pb2.Subscribe_FlowUnit_Responses.FlowUnit_Struct(
                    VolumeUnit=PumpUnitController_pb2.DataType_VolumeUnit(
                        VolumeUnit=silaFW_pb2.String(
                            value=volume_unit
                        )
                    ),
                    TimeUnit=PumpUnitController_pb2.DataType_TimeUnit(
                        TimeUnit=silaFW_pb2.String(
                            value=time_unit
                        )
                    )
                )
            )
            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)

    def Subscribe_VolumeUnit(self, request, context: grpc.ServicerContext) \
            -> PumpUnitController_pb2.Subscribe_VolumeUnit_Responses:
        """
        Requests the observable property Volume Unit
            The currently used volume unit.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            request.VolumeUnit (Volume Unit): The currently used volume unit.
        """

        while True:
            yield PumpUnitController_pb2.Subscribe_VolumeUnit_Responses(
                VolumeUnit=PumpUnitController_pb2.DataType_VolumeUnit(
                    VolumeUnit=silaFW_pb2.String(
                        value=uc.volume_unit_to_string(self.pump.get_volume_unit())
                    )
                )
            )
            # we add a small delay to give the client a chance to keep up.
            time.sleep(0.5)
