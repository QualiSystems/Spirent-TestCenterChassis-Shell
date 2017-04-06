#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `TestCenterChassisDriver`
"""

import unittest

from cloudshell.shell.core.driver_context import (ConnectivityContext, ResourceContextDetails, InitCommandContext)
from src.stc_handler import StcHandler

address = '10.224.18.200'
client_install_path = 'C:/Program Files (x86)/Spirent Communications/Spirent TestCenter 4.71'


class TestTestCenterChassisDriver(unittest.TestCase):

    def setUp(self):
        self.connectivity = ConnectivityContext(None, None, None, None)
        self.resource = ResourceContextDetails(None, None, None, None, None, None, None, None, None, None)
        self.resource.address = address
        self.resource.attributes = {'Client Install Path': client_install_path}
        self.context = InitCommandContext(self.connectivity, self.resource)
        self.handler = StcHandler()
        self.handler.initialize(self.context)

    def tearDown(self):
        pass

    def testAutoload(self):
        context = InitCommandContext(self.connectivity, self.resource)
        inventory = self.handler.get_inventory(context)
        for r in inventory.resources:
            print r.relative_address, r.model, r.name
        for a in inventory.attributes:
            print a.relative_address, a.attribute_name, a.attribute_value


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())