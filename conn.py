#!/usr/bin/env python
from genie.testbed import load

base_tb = load('tb-1-device.yaml')
testbed = load('tb-2-device.yaml')

xe1 = base_tb.devices['xe1']

xe1.connect(log_stdout=False)

xe1_acl = xe1.parse('show access-list')

#for device_name, device in testbed.devices.items():
#    print(device)
#    print(device_name)
#    device_name.connect()

for name, dev in testbed.devices.items():
    dev.connect(log_stdout=False)
    #print(name)
    #print(dev)
    xe_acl = dev.parse('show access-list')
    for acl in xe_acl:
        if acl not in xe1_acl:
            print(f"ACL on router {name} is not found")
        else:
            print(f"ACL on router {name} is compliant")
