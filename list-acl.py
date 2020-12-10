#!/usr/bin/env python
from genie.testbed import load
from genie.utils.diff import Diff


testbed_1 = load('tb-1-device.yaml')
testbed_2 = load('tb-2-device.yaml')

xe1=testbed_1.devices['xe1']

xe1.connect(log_stdout=False)

acl_list = xe1.parse('show access-list')

acl_id = '100'

base_acl = (acl_list[acl_id])
#print(base_acl)

for name, dev in testbed_2.devices.items():
    dev.connect(log_stdout=False)
    all_acl=dev.parse('show access-list')
    compare_acl=(all_acl[acl_id])
    #print(f"ACL on router {name} is: \n" + str(compare_acl))
    diff = Diff(base_acl, compare_acl)
    diff.findDiff()
    #print(bool(diff))
    #print(bool(str(diff)))
    #print(f"ACL {acl_id} differences on router {name} \n" + str(diff))
    #print(diff)
    if str(diff):
        print(f"ACL {acl_id} on router {name} is not compliant")
    else:
        print(f"ACL {acl_id} on router {name} is compliant")

#for acl in acl_list:
    #print(acl_list[acl]['name'])
    #print(acl_list[acl])
    #print(acl_list[acl_id])
    #po1=(acl_list[acl_id])
    #print(po1)