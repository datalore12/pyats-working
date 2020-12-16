#!/usr/bin/env python3

# To get a logger for the script
import logging

from pyats import aetest
from pyats.log.utils import banner

# Genie Imports
from genie.conf import Genie

# To handle erorrs in connections
from unicon.core import errors

import argparse
from pyats.topology import loader

# Get your logger for your script
global log
log = logging.getLogger(__name__)
log.level = logging.INFO

class MyCommonSetup(aetest.CommonSetup):
    """
    CommonSetup class to prepare for testcases
    Establishes connections to all devices in testbed
    """

    @aetest.subsection
    def establish_connections(self, testbed):
        """
        Establishes connections to all devices in testbed
        :param testbed:
        :return:
        """

        genie_testbed = Genie.init(testbed)
        self.parent.parameters['testbed'] = genie_testbed
        device_list = []
        for device in genie_testbed.devices.values():
            log.info(banner(
                f"Connect to device '{device.name}'"))
            try:
                device.connect(log_stdout=False)
            except errors.ConnectionError:
                self.failed(f"Failed to establish "
                            f"connection to '{device.name}'")
            device_list.append(device)
        # Pass list of devices to testcases
        self.parent.parameters.update(dev=device_list)


class Routing(aetest.Testcase):
    """
    Routing Testcase - extract routing information from devices
    Verify that all device have golden_routes installed in RIB
    """

    @aetest.setup
    def setup(self):
        """
        Get list of all devices in testbed and
        run routes testcase for each device
        :return:
        """

        devices = self.parent.parameters['dev']
        aetest.loop.mark(self.routes, device=devices)



    @aetest.test
    def routes(self, device):
        """
        Verify that Gi0/0/0/0 OSPF Cost is 10
        """

        output = device.parse('show ospf vrf all-inclusive interface gi0/0/0/0')

        ospf_int_cost=(output['vrf']['']['address_family']['ipv4']['instance']['1']['areas']['0.0.0.0']['interfaces']['GigabitEthernet0/0/0/0']['cost'])

        if ospf_int_cost != 10:
            self.failed('Cost is not 10')
        else:
            pass


if __name__ == '__main__':  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest='testbed',
                        type=loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
