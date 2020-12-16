#!/usr/bin/env python

from pyats import aetest
from genie.testbed import load
from pyats.log.utils import banner
import argparse
import logging



testbed = load('tb-1-device.yaml')

global log
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_device(self):
        # connect to testbed devices
        for device in testbed:
            log.info(banner(f"Connect to device '{device.name}'"))
            try:
                device.connect(log_stdout=False)
            except errors.ConnectionError:
                self.failed(f"Failed to establish "
                            f"connection to '{device.name}'")

# for running as its own executable
if __name__ == '__main__':
    aetest.main()