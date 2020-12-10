#!/usr/bin/env python
from genie.testbed import load

# Load testbed-file 
testbed = load('xr-tb-all.yaml')

xr1 = testbed.devices['xr1']
xr1.connect(log_stdout=False)

acl_id='100'
#ver = xe1.parse('show version')
xr1_acl = xr1.parse('show access-lists afi-all')

#hostname=(ver['version']['hostname'])
acl_name=(xr1_acl[acl_id]['name'])

#print(f"Hostname for this router is {hostname}")
#print(xr1_acl)
print(acl_name)
print("\n")
print(f"ACL {acl_name}")



