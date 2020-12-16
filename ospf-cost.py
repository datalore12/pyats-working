#!/usr/bin/env python
from genie.testbed import load

testbed = load('tb.yaml')

xr1 = testbed.devices['xr1']

xr1.connect(log_stdout=False)

ospf_info=xr1.parse('show ospf vrf all-inclusive interface gi0/0/0/0')

ospf_int_cost=(ospf_info['vrf']['']['address_family']['ipv4']['instance']['1']['areas']['0.0.0.0']['interfaces']['GigabitEthernet0/0/0/0']['cost'])

int_name=(ospf_info['GigabitEthernet0/0/0/0']['cost'])

print(ospf_int_cost)
print('\n')
print(int_name)