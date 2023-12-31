#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: sila_cetoni

*QmixControl client*

:details: QmixControl:
    The SiLA 2 driver for Qmix Control Devices

:file:    BatteryProvider_client.py
:authors: Florian Meinicke

:date: (creation)          2021-04-20T06:40:37.451567
:date: (last modification) 2021-04-20T06:40:37.451567

.. note:: Code generated by sila2codegenerator 0.3.6

_______________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""
__version__ = "0.1.0"

# import general packages
import logging
import argparse
import grpc
import time
import datetime

# import meta packages
from typing import Union, Optional

# import SiLA2 library modules
from sila2lib.framework import SiLAFramework_pb2 as silaFW_pb2
from sila2lib.sila_client import SiLA2Client
from sila2lib.framework.std_features import SiLAService_pb2 as SiLAService_feature_pb2
from sila2lib.error_handling import client_err
#   Usually not needed, but - feel free to modify
# from sila2lib.framework.std_features import SimulationController_pb2 as SimController_feature_pb2

# import feature gRPC modules
# Import gRPC libraries of features
from impl.de.cetoni.core.BatteryProvider.gRPC import BatteryProvider_pb2
from impl.de.cetoni.core.BatteryProvider.gRPC import BatteryProvider_pb2_grpc
# import default arguments for this feature
from impl.de.cetoni.core.BatteryProvider.BatteryProvider_default_arguments import default_dict as BatteryProvider_default_dict


# noinspection PyPep8Naming, PyUnusedLocal
class BatteryProviderClient:
    """
        The SiLA 2 driver for Qmix Control Devices

    .. note:: For an example on how to construct the parameter or read the response(s) for command calls and properties,
              compare the default dictionary that is stored in the directory of the corresponding feature.
    """
    # The following variables will be filled when run() is executed
    #: Storage for the connected servers version
    server_version: str = ''
    #: Storage for the display name of the connected server
    server_display_name: str = ''
    #: Storage for the description of the connected server
    server_description: str = ''

    def __init__(self,
                 channel = None):
        """Class initialiser"""

        # Create stub objects used to communicate with the server
        self.BatteryProvider_stub = \
            BatteryProvider_pb2_grpc.BatteryProviderStub(channel)


        # initialise class variables for server information storage
        self.server_version = ''
        self.server_display_name = ''
        self.server_description = ''



    def Subscribe_BatteryVoltage(self) \
            -> BatteryProvider_pb2.Subscribe_BatteryVoltage_Responses:
        """Wrapper to get property BatteryVoltage from the server."""
        # noinspection PyUnusedLocal - type definition, just for convenience
        grpc_err: grpc.Call

        logging.debug("Reading observable property BatteryVoltage:")
        try:
            response = self.BatteryProvider_stub.Subscribe_BatteryVoltage(
                BatteryProvider_pb2.Subscribe_BatteryVoltage_Parameters()
            )
            logging.debug(
                'Subscribe_BatteryVoltage response: {response}'.format(
                    response=response
                )
            )
        except grpc.RpcError as grpc_err:
            self.grpc_error_handling(grpc_err)
            return None

        return response


    @staticmethod
    def grpc_error_handling(error_object: grpc.Call) -> None:
        """Handles exceptions of type grpc.RpcError"""
        # pass to the default error handling
        grpc_error =  client_err.grpc_error_handling(error_object=error_object)

        logging.error(grpc_error.error_type)
        if hasattr(grpc_error.message, "parameter"):
            logging.error(grpc_error.message.parameter)
        logging.error(grpc_error.message.message)


