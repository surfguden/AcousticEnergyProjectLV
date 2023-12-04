#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Qmix Control*

:details: Qmix Control:
    The SiLA 2 driver for Qmix Control Devices

:file:    Qmix Control_server.py
:authors: Florian Meinicke

:date: (creation)          2020-10-08T09:17:41.398349
:date: (last modification) 2020-10-08T09:17:41.398349

.. note:: Code generated by sila2codegenerator 0.2.0

________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""
__version__ = "0.1.0"

import logging
import argparse
import os

# Import the main SiLA library
from sila2lib.sila_server import SiLA2Server

# Import gRPC libraries of features
from impl.de.cetoni.controllers.ControlLoopService.gRPC import ControlLoopService_pb2
from impl.de.cetoni.controllers.ControlLoopService.gRPC import ControlLoopService_pb2_grpc
# import default arguments for this feature
from impl.de.cetoni.controllers.ControlLoopService.ControlLoopService_default_arguments import default_dict as ControlLoopService_default_dict
from impl.de.cetoni.core.ChannelGatewayService.gRPC import ChannelGatewayService_pb2
from impl.de.cetoni.core.ChannelGatewayService.gRPC import ChannelGatewayService_pb2_grpc
# import default arguments for this feature
from impl.de.cetoni.core.ChannelGatewayService.ChannelGatewayService_default_arguments import default_dict as ChannelGatewayService_default_dict

# Import the servicer modules for each feature
from impl.de.cetoni.controllers.ControlLoopService.ControlLoopService_servicer import ControlLoopService
from impl.de.cetoni.core.ChannelGatewayService.ChannelGatewayService_servicer import ChannelGatewayService
from ..local_ip import LOCAL_IP

class QmixControlServer(SiLA2Server):
    """
    The SiLA 2 driver for Qmix Control Devices
    """

    def __init__(self, cmd_args, controller_channels, simulation_mode: bool = True):
        """
        Class initialiser

            :param cmd_args: Arguments that were given on the command line
            :param controller_channels: The qmixcontroller.Controller objects that this server shall use
            :param simulation_mode: Sets whether at initialisation the simulation mode is active or the real mode
        """
        super().__init__(
            name=cmd_args.server_name, description=cmd_args.description,
            server_type=cmd_args.server_type, server_uuid=None,
            version=__version__,
            vendor_url="cetoni.de",
            ip=LOCAL_IP, port=int(cmd_args.port),
            key_file=cmd_args.encryption_key, cert_file=cmd_args.encryption_cert,
            simulation_mode=simulation_mode
        )

        logging.info(
            "Starting SiLA2 server with server name: {server_name}".format(
                server_name=cmd_args.server_name
            )
        )

        meta_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..',
                                                 'features', 'de', 'cetoni', 'controllers'))

        # registering features
        #  Register de.cetoni.core.ChannelGatewayService
        self.ChannelGatewayService_servicer = ChannelGatewayService(
            channels=controller_channels,
            simulation_mode=self.simulation_mode
        )
        ChannelGatewayService_pb2_grpc.add_ChannelGatewayServiceServicer_to_server(
            self.ChannelGatewayService_servicer,
            self.grpc_server
        )
        self.add_feature(feature_id='de.cetoni/core/ChannelGatewayService/v1',
                         servicer=self.ChannelGatewayService_servicer,
                         data_path=meta_path.replace('controllers', 'core'))
        #  Register de.cetoni.controllers.ControlLoopService
        self.ControlLoopService_servicer = ControlLoopService(
            channel_gateway=self.ChannelGatewayService_servicer,
            simulation_mode=self.simulation_mode
        )
        ControlLoopService_pb2_grpc.add_ControlLoopServiceServicer_to_server(
            self.ControlLoopService_servicer,
            self.grpc_server
        )
        self.add_feature(feature_id='de.cetoni/controllers/ControlLoopService/v1',
                         servicer=self.ControlLoopService_servicer,
                         data_path=meta_path)

        self.simulation_mode = simulation_mode


def parse_command_line():
    """
    Just looking for commandline arguments
    """
    parser = argparse.ArgumentParser(description="A SiLA2 service: Qmix Control")

    # Simple arguments for the server identification
    parser.add_argument('-s', '--server-name', action='store',
                        default="Qmix Control", help='start SiLA server with [server-name]')
    parser.add_argument('-t', '--server-type', action='store',
                        default="Unknown Type", help='start SiLA server with [server-type]')
    parser.add_argument('-d', '--description', action='store',
                        default="The SiLA 2 driver for Qmix Control Devices", help='SiLA server description')

    # Encryption
    parser.add_argument('-X', '--encryption', action='store', default=None,
                        help='The name of the private key and certificate file (without extension).')
    parser.add_argument('--encryption-key', action='store', default=None,
                        help='The name of the encryption key (*with* extension). Can be used if key and certificate '
                             'vary or non-standard file extensions are used.')
    parser.add_argument('--encryption-cert', action='store', default=None,
                        help='The name of the encryption certificate (*with* extension). Can be used if key and '
                             'certificate vary or non-standard file extensions are used.')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)

    parsed_args = parser.parse_args()

    # validate/update some settings
    #   encryption
    if parsed_args.encryption is not None:
        # only overwrite the separate keys if not given manually
        if parsed_args.encryption_key is None:
            parsed_args.encryption_key = parsed_args.encryption + '.key'
        if parsed_args.encryption_cert is None:
            parsed_args.encryption_cert = parsed_args.encryption + '.cert'

    return parsed_args


if __name__ == '__main__':
    # or use logging.ERROR for less output
    logging.basicConfig(format='%(levelname)-8s| %(module)s.%(funcName)s: %(message)s', level=logging.DEBUG)

    args = parse_command_line()

    # generate SiLA2Server
    sila_server = QmixControlServer(cmd_args=args, simulation_mode=True)
