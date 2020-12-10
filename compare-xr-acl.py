#!/usr/bin/env python
from genie.testbed import load
from genie.utils.diff import Diff

# Load the different testbeds for base router and comparing routers
testbed_1 = load('xr-tb-1.yaml')
testbed_2 = load('xr-tb-2.yaml')

#Connect to xe1 and extract ACLs
xr1=testbed_1.devices['xr1']
xr1.connect(log_stdout=False)
acl_list = xr1.parse('show access-list afi-all')

# Identify target ACL to compare and assign it to variable base_acl
acl_id = '100'
base_acl = (acl_list[acl_id])

# connect to all other routers, extract ACL and diff out the differences
for name, dev in testbed_2.devices.items():
    dev.connect(log_stdout=False)
    all_acl=dev.parse('show access-list afi-all')
    compare_acl=(all_acl[acl_id])
    diff = Diff(base_acl, compare_acl)
    diff.findDiff()
    if str(diff):
        print(f"ACL {acl_id} on router {name} is not compliant")
    else:
        print(f"ACL {acl_id} on router {name} is compliant")
