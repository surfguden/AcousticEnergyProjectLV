"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Pump Fluid Dosing Service*

:details: PumpFluidDosingService:
    Allows to dose a specified fluid. There are commands for absolute dosing (SetFillLevel) and relative dosing
    (DoseVolume and GenerateFlow) available.The flow rate can be negative. In this case the pump aspirates the fluid
    instead of dispensing. The flow rate has to be a value between MaxFlowRate and MinFlowRate. If the value is not
    within this range (hence is invalid) a ValidationError will be thrown.
    At any time the property CurrentSyringeFillLevel can be queried to see how much fluid is left in the syringe.
    Similarly the property CurrentFlowRate can be queried to get the current flow rate at which the pump is dosing.

:file:    PumpFluidDosingService_servicer.py
:authors: Florian Meinicke

:date: (creation)          2019-07-16T11:11:31.295448
:date: (last modification) 2019-10-05T11:53:30.831212

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
from impl.common.qmix_errors import SiLAFrameworkError, SiLAValidationError, QmixSDKSiLAError, DeviceError

# import gRPC modules for this feature
from .gRPC import PumpFluidDosingService_pb2 as PumpFluidDosingService_pb2
from .gRPC import PumpFluidDosingService_pb2_grpc as PumpFluidDosingService_pb2_grpc

# import simulation and real implementation
from .PumpFluidDosingService_simulation import PumpFluidDosingServiceSimulation
from .PumpFluidDosingService_real import PumpFluidDosingServiceReal


class PumpFluidDosingService(PumpFluidDosingService_pb2_grpc.PumpFluidDosingServiceServicer):
    """
    This is a sample service for controlling neMESYS syringe pumps via SiLA2
    """
    implementation: Union[PumpFluidDosingServiceSimulation, PumpFluidDosingServiceReal]
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
                               implementation: Union[PumpFluidDosingServiceSimulation,
                                                     PumpFluidDosingServiceReal]
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
        self._inject_implementation(PumpFluidDosingServiceSimulation())

    def switch_to_real_mode(self):
        """Method that will automatically be called by the server when the real mode is requested."""
        self.simulation_mode = False
        self._inject_implementation(PumpFluidDosingServiceReal(self.pump))

    def SetFillLevel(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Set Fill Level"
            Pumps fluid with the given flow rate until the requested fill level is reached.
            Depending on the requested fill level given in the FillLevel parameter this function may cause aspiration or dispension of fluid.

        :param request: gRPC request containing the parameters passed:
            request.FillLevel (Fill Level):
            The requested fill level. A level of 0 indicates a completely empty syringe. The value has to be between 0 and MaxSyringeFillLevel. Depending on the requested fill level this may cause aspiration or dispension of fluid.
            request.FlowRate (Flow Rate):
            The flow rate at which the pump should dose the fluid.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        logging.debug(
            "SetFillLevel called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.SetFillLevel(request, context)
        except (SiLAValidationError, DeviceError) as err:
            self.implementation.StopDosage(None, None)
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)
            return None

    def SetFillLevel_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.SetFillLevel`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """

        logging.debug(
            "SetFillLevel_Info called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            for value in self.implementation.SetFillLevel_Info(request, context):
                yield value
        except SiLAFrameworkError as err:
            err.raise_rpc_error(context)

    def SetFillLevel_Result(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.SetFillLevel_Responses:
        """
        Returns the final result of the command call :meth:`~.SetFillLevel`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "SetFillLevel_Result called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.SetFillLevel_Result(request, context)
        except SiLAFrameworkError as err:
            err.raise_rpc_error(context)


    def DoseVolume(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Dose Volume"
            Dose a certain amount of volume with the given flow rate.

        :param request: gRPC request containing the parameters passed:
            request.Volume (Volume):
            The amount of volume to dose. This value can be negative. In that case the pump aspirates the fluid.
            request.FlowRate (Flow Rate): The flow rate at which the pump should dose the fluid.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        logging.debug(
            "DoseVolume called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.DoseVolume(request, context)
        except (SiLAValidationError, DeviceError) as err:
            self.implementation.StopDosage(None, None)
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)

    def DoseVolume_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.DoseVolume`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """

        logging.debug(
            "DoseVolume_Info called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            for value in self.implementation.DoseVolume_Info(request, context):
                yield value
        except SiLAFrameworkError as err:
            err.raise_rpc_error(context)

    def DoseVolume_Result(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.DoseVolume_Responses:
        """
        Returns the final result of the command call :meth:`~.DoseVolume`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "DoseVolume_Result called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.DoseVolume_Result(request, context)
        except SiLAFrameworkError as err:
            err.raise_rpc_error(context)


    def GenerateFlow(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Generate Flow"
            Generate a continous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

        :param request: gRPC request containing the parameters passed:
            request.FlowRate (Flow Rate):
            The flow rate at which the pump should dose the fluid. This value can be negative. In that case the pump aspirates the fluid.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A command confirmation object with the following information:
            commandId: A command id with which this observable command can be referenced in future calls
            lifetimeOfExecution: The (maximum) lifetime of this command call.
        """

        logging.debug(
            "GenerateFlow called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.GenerateFlow(request, context)
        except (SiLAValidationError, DeviceError) as err:
            self.implementation.StopDosage(None, None)
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)

    def GenerateFlow_Info(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.ExecutionInfo:
        """
        Returns execution information regarding the command call :meth:`~.GenerateFlow`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: An ExecutionInfo response stream for the command with the following fields:
            commandStatus: Status of the command (enumeration)
            progressInfo: Information on the progress of the command (0 to 1)
            estimatedRemainingTime: Estimate of the remaining time required to run the command
            updatedLifetimeOfExecution: An update on the execution lifetime
        """

        logging.debug(
            "GenerateFlow_Info called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            for value in self.implementation.GenerateFlow_Info(request, context):
                yield value
        except SiLAFrameworkError as err:
            err.raise_rpc_error(context)

    def GenerateFlow_Result(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.GenerateFlow_Responses:
        """
        Returns the final result of the command call :meth:`~.GenerateFlow`.

        :param request: A request object with the following properties
            CommandExecutionUUID: The UUID of the command executed.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "GenerateFlow_Result called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.GenerateFlow_Result(request, context)
        except SiLAFrameworkError as err:
            err.raise_rpc_error(context)


    def StopDosage(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.StopDosage_Responses:
        """
        Executes the unobservable command "Stop Dosage"
            Stops a currently running dosage immediately.

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            request.EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        logging.debug(
            "StopDosage called in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            return self.implementation.StopDosage(request, context)
        except DeviceError as err:
            err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)

    def Subscribe_MaxSyringeFillLevel(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.Subscribe_MaxSyringeFillLevel_Responses:
        """
        Requests the observable property Maximum Syringe Fill Level
            The maximum amount of fluid that the syringe can hold.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.MaxSyringeFillLevel (Maximum Syringe Fill Level): The maximum amount of fluid that the syringe can hold.
        """

        logging.debug(
            "Property MaxSyringeFillLevel requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            for value in self.implementation.Subscribe_MaxSyringeFillLevel(request, context):
                yield value
        except DeviceError as err:
            err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)

    def Subscribe_SyringeFillLevel(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.Subscribe_SyringeFillLevel_Responses:
        """
        Requests the observable property Syringe Fill Level
            The current amount of fluid left in the syringe.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.SyringeFillLevel (Syringe Fill Level): The current amount of fluid left in the syringe.
        """

        logging.debug(
            "Property SyringeFillLevel requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            for value in self.implementation.Subscribe_SyringeFillLevel(request, context):
                yield value
        except DeviceError as err:
            err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)

    def Subscribe_MaxFlowRate(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.Subscribe_MaxFlowRate_Responses:
        """
        Requests the observable property Maximum Flow Rate
            The maximum value of the flow rate at which this pump can dose a fluid.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.MaxFlowRate (Maximum Flow Rate): The maximum value of the flow rate at which this pump can dose a fluid.
        """

        logging.debug(
            "Property MaxFlowRate requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            for value in self.implementation.Subscribe_MaxFlowRate(request, context):
                yield value
        except DeviceError as err:
            err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)

    def Subscribe_FlowRate(self, request, context: grpc.ServicerContext) \
            -> PumpFluidDosingService_pb2.Subscribe_FlowRate_Responses:
        """
        Requests the observable property Flow Rate
            The current value of the flow rate. It is 0 if the pump does not dose any fluid.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.FlowRate (Flow Rate): The current value of the flow rate. It is 0 if the pump does not dose any fluid.
        """

        logging.debug(
            "Property FlowRate requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )

        try:
            for value in self.implementation.Subscribe_FlowRate(request, context):
                yield value
        except DeviceError as err:
            err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context)
