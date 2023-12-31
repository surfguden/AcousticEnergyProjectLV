"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Continuous Flow Dosing Service*

:details: ContinuousFlowDosingService:
    Allows to continuously dose a specified fluid.
    The continuous flow mode is meant for dispensing volumes or generating flows and works only in one direction. That
    means using negative flow rates or negative volumes for aspiration is not possible.

:file:    ContinuousFlowDosingService_servicer.py
:authors: Florian Meinicke

:date: (creation)          2020-10-22T12:16:33.376426
:date: (last modification) 2020-10-22T12:16:33.376426

.. note:: Code generated by sila2codegenerator 0.3.2.dev

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
# import SiLA errors
from impl.common.qmix_errors import SiLAFrameworkError, SiLAValidationError, QmixSDKSiLAError, DeviceError

# import gRPC modules for this feature
from .gRPC import ContinuousFlowDosingService_pb2 as ContinuousFlowDosingService_pb2
from .gRPC import ContinuousFlowDosingService_pb2_grpc as ContinuousFlowDosingService_pb2_grpc

# import simulation and real implementation
from .ContinuousFlowDosingService_simulation import ContinuousFlowDosingServiceSimulation
from .ContinuousFlowDosingService_real import ContinuousFlowDosingServiceReal

class ContinuousFlowDosingService(ContinuousFlowDosingService_pb2_grpc.ContinuousFlowDosingServiceServicer):
    """
    Allows to control a continuous flow pump that is made up of two syringe pumps
    """
    implementation: Union[ContinuousFlowDosingServiceSimulation, ContinuousFlowDosingServiceReal]
    simulation_mode: bool

    def __init__(self, pump, simulation_mode: bool = True):
        """
        Class initialiser.

        :param pump: A valid `qxmixpump.ContiFlowPump` for this service to use
        :param simulation_mode: Sets whether at initialisation the simulation mode is active or the real mode
        """

        self.pump = pump

        self.simulation_mode = simulation_mode
        if simulation_mode:
            self.switch_to_simulation_mode()
        else:
            self.switch_to_real_mode()

    def _inject_implementation(self,
                               implementation: Union[ContinuousFlowDosingServiceSimulation,
                                                     ContinuousFlowDosingServiceReal]
                               ) -> bool:
        """
        Dependency injection of the implementation used.
            Allows to set the class used for simulation/real mode.

        :param implementation: A valid implementation of the ContiflowServicer.
        """

        self.implementation = implementation
        return True

    def switch_to_simulation_mode(self):
        """Method that will automatically be called by the server when the simulation mode is requested."""
        self.simulation_mode = True
        self._inject_implementation(ContinuousFlowDosingServiceSimulation())

    def switch_to_real_mode(self):
        """Method that will automatically be called by the server when the real mode is requested."""
        self.simulation_mode = False
        self._inject_implementation(ContinuousFlowDosingServiceReal(self.pump))

    def GenerateFlow(self, request, context: grpc.ServicerContext) \
            -> silaFW_pb2.CommandConfirmation:
        """
        Executes the observable command "Generate Flow"
            Generate a continuous flow with the given flow rate. Dosing continues until it gets stopped manually by calling StopDosage or until the pusher reached one of its limits.

        :param request: gRPC request containing the parameters passed:
            request.FlowRate (Flow Rate): The flow rate at which the pump should dose the fluid. This value cannot be negative since dosing is meant to only work in one direction.
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
            return None

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
            return None

    def GenerateFlow_Result(self, request, context: grpc.ServicerContext) \
            -> ContinuousFlowDosingService_pb2.GenerateFlow_Responses:
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
            return None


    def StopDosage(self, request, context: grpc.ServicerContext) \
            -> ContinuousFlowDosingService_pb2.StopDosage_Responses:
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
            return None

    def Subscribe_MaxFlowRate(self, request, context: grpc.ServicerContext) \
            -> ContinuousFlowDosingService_pb2.Subscribe_MaxFlowRate_Responses:
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
            return None

    def Subscribe_FlowRate(self, request, context: grpc.ServicerContext) \
            -> ContinuousFlowDosingService_pb2.Subscribe_FlowRate_Responses:
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
            return None

