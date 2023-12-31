#!/usr/bin/env python3
"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Battery test client*

:details: Battery:
    A device that is powered by a battery

:file:    Battery_testclient.py
:authors: Florian Meinicke

:date: (creation)          2021-04-20T09:23:16.468839
:date: (last modification) 2021-04-20T09:23:16.468839

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
import time
import datetime

# import meta packages
from typing import Union, Optional

# import SiLA client module
from .Battery_client import BatteryClient


def parse_command_line():
    """
    Just looking for command line arguments
    """
    parser = argparse.ArgumentParser(
        description="A SiLA2 test client for: Battery")

    # connection parameters
    parser.add_argument('-i', '--server-ip-address', action='store', default='127.0.0.1',
                        help='SiLA server IP address')
    parser.add_argument('--server-hostname', action='store', default='localhost',
                        help='SiLA server hostname')
    parser.add_argument('-p', '--server-port', action='store', default=50052,
                        help='SiLA server port')

    # encryption
    parser.add_argument('-X', '--encryption', action='store', default='sila2_server',
                        help='The name of the private key and certificate file (without extension).')
    parser.add_argument('--encryption-key', action='store', default=None,
                        help='The name of the encryption key (*with* extension). Can be used if key and certificate '
                             'vary or non-standard file extensions are used.')
    parser.add_argument('--encryption-cert', action='store', default=None,
                        help='The name of the encryption certificate (*with* extension). Can be used if key and '
                             'certificate vary or non-standard file extensions are used.')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__)

    return parser.parse_args()


if __name__ == '__main__':
    # or use logging.INFO (=20) or logging.ERROR (=30) for less output
    logging.basicConfig(
        format='%(levelname)-8s| %(module)s.%(funcName)s: %(message)s', level=logging.DEBUG)

    parsed_args = parse_command_line()

    # start the client
    sila_client = BatteryClient(server_ip=parsed_args.server_ip_address,
                                        server_port=int(parsed_args.server_port))
    sila_client.run()

    # Log connection info
    logging.info(
        (
            f'Connected to SiLA Server {sila_client.server_display_name} running in version {sila_client.server_version}.' '\n'
            f'Service description: {sila_client.server_description}'
        )
    )

    # TODO:
    #   Uncomment the calls you would like to test and remove type hints (given only for orientation) or
    #   write your further function calls here to run the client as a standalone application.

    # ------------- command calls -------------------

    # ----- de/cetoni/core/BatteryProvider

    # ------------- property calls -------------------

    # ----- de/cetoni/core/BatteryProvider
    # results = sila_client.de/cetoni/core/BatteryProvider_client.BatteryVoltage()
    # print("BatteryVoltage res: ", results)


