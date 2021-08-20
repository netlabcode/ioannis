#Topology Substation 13-10-11
#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Node, Controller, RemoteController, OVSSwitch, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.link import Intf, TCLink
from mininet.log import setLogLevel, info
from mininet.node import Node, CPULimitedHost
from mininet.util import irange,dumpNodeConnections
import time
import os


class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

def emptyNet():

    NODE2_IP='192.168.56.1'
    CONTROLLER_IP='127.0.0.1'

    net = Mininet( topo=None,
                   build=False)

    #c0 = net.addController( 'c0',controller=RemoteController,ip=CONTROLLER_IP,port=6633)
    net.addController('c0', port=6633)

    r0 = net.addHost('r0', cls=LinuxRouter, ip='100.0.0.1/16')
    r5 = net.addHost('r5', cls=LinuxRouter, ip='100.5.0.1/16')
    r6 = net.addHost('r6', cls=LinuxRouter, ip='100.6.0.1/16')
    r7 = net.addHost('r7', cls=LinuxRouter, ip='100.7.0.1/16')
    r21 = net.addHost('r21', cls=LinuxRouter, ip='100.21.0.1/16')
    r24 = net.addHost('r24', cls=LinuxRouter, ip='100.24.0.1/16')
    r8 = net.addHost('r8', cls=LinuxRouter, ip='100.8.0.1/16')

    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s51 = net.addSwitch( 's51' )
    s52 = net.addSwitch( 's52' )
    s53 = net.addSwitch( 's53' )
    s61 = net.addSwitch( 's61' )
    s62 = net.addSwitch( 's62' )
    s63 = net.addSwitch( 's63' )
    s71 = net.addSwitch( 's71' )
    s72 = net.addSwitch( 's72' )
    s73 = net.addSwitch( 's73' )
    s211 = net.addSwitch( 's211' )
    s212 = net.addSwitch( 's212' )
    s213 = net.addSwitch( 's213' )
    s241 = net.addSwitch( 's241' )
    s242 = net.addSwitch( 's242' )
    s243 = net.addSwitch( 's243' )
    s81 = net.addSwitch( 's81' )
    s82 = net.addSwitch( 's82' )
    s83 = net.addSwitch( 's83' )

    # Add host-switch links in the same subnet
    net.addLink(s999, r0, intfName2='r0-eth1', params2={'ip': '100.0.0.1/16'})
    net.addLink(s51, r5, intfName2='r5-eth1', params2={'ip': '100.5.0.1/16'})
    net.addLink(s61, r6, intfName2='r6-eth1', params2={'ip': '100.6.0.1/16'})
    net.addLink(s71, r7, intfName2='r7-eth1', params2={'ip': '100.7.0.1/16'})
    net.addLink(s211, r21, intfName2='r21-eth1', params2={'ip': '100.21.0.1/16'})
    net.addLink(s241, r24, intfName2='r24-eth1', params2={'ip': '100.24.0.1/16'})
    net.addLink(s81, r8, intfName2='r8-eth1', params2={'ip': '100.8.0.1/16'})

    # Add router-router link in a new subnet for the router-router connection
    net.addLink(r0, r5, intfName1='r0-eth2', intfName2='r5-eth2', params1={'ip': '200.5.0.1/24'}, params2={'ip': '200.5.0.2/24'})
    net.addLink(r0, r6, intfName1='r0-eth3', intfName2='r6-eth2', params1={'ip': '200.6.0.1/24'}, params2={'ip': '200.6.0.2/24'})
    net.addLink(r0, r7, intfName1='r0-eth4', intfName2='r7-eth2', params1={'ip': '200.7.0.1/24'}, params2={'ip': '200.7.0.2/24'})
    net.addLink(r0, r21, intfName1='r0-eth5', intfName2='r21-eth2', params1={'ip': '200.21.0.1/24'}, params2={'ip': '200.21.0.2/24'})
    net.addLink(r0, r24, intfName1='r0-eth6', intfName2='r24-eth2', params1={'ip': '200.24.0.1/24'}, params2={'ip': '200.24.0.2/24'})
    net.addLink(r0, r8, intfName1='r0-eth7', intfName2='r8-eth2', params1={'ip': '200.8.0.1/24'}, params2={'ip': '200.8.0.2/24'})

    # Add Host on Control Center
    ccdb = net.addHost('ccdb', ip='100.0.0.11')
    cctl = net.addHost('cctl', ip='100.0.0.12')

    # Add Hosts on Substation 5
    s05m1 = net.addHost('s05m1', ip='100.5.0.11', cls=CPULimitedHost, cpu=.1)
    s05m2 = net.addHost('s05m2', ip='100.5.0.12', cls=CPULimitedHost, cpu=.1)
    s05m3 = net.addHost('s05m3', ip='100.5.0.13', cls=CPULimitedHost, cpu=.1)
    s05m4 = net.addHost('s05m4', ip='100.5.0.14', cls=CPULimitedHost, cpu=.1)
    s05m5 = net.addHost('s05m5', ip='100.5.0.15', cls=CPULimitedHost, cpu=.1)
    s05m6 = net.addHost('s05m6', ip='100.5.0.16', cls=CPULimitedHost, cpu=.1)
    s05cpc = net.addHost('s05cpc', ip='100.5.0.21')
    s05db = net.addHost('s05db', ip='100.5.0.22')
    s05gw = net.addHost('s05gw', ip='100.5.0.23')

    # Add Hosts on Substation 6
    s06m1 = net.addHost('s06m1', ip='100.6.0.11', cls=CPULimitedHost, cpu=.1)
    s06m2 = net.addHost('s06m2', ip='100.6.0.12', cls=CPULimitedHost, cpu=.1)
    s06m3 = net.addHost('s06m3', ip='100.6.0.13', cls=CPULimitedHost, cpu=.1)
    s06m4 = net.addHost('s06m4', ip='100.6.0.14', cls=CPULimitedHost, cpu=.1)
    s06m5 = net.addHost('s06m5', ip='100.6.0.15', cls=CPULimitedHost, cpu=.1)
    s06m6 = net.addHost('s06m6', ip='100.6.0.16', cls=CPULimitedHost, cpu=.1)
    s06m7 = net.addHost('s06m7', ip='100.6.0.17', cls=CPULimitedHost, cpu=.1)
    s06m8 = net.addHost('s06m8', ip='100.6.0.18', cls=CPULimitedHost, cpu=.1)
    s06m9 = net.addHost('s06m9', ip='100.6.0.19', cls=CPULimitedHost, cpu=.1)
    s06cpc = net.addHost('s06cpc', ip='100.6.0.21')
    s06db = net.addHost('s06db', ip='100.6.0.22')
    s06gw = net.addHost('s06gw', ip='100.6.0.23')

    # Add Hosts on Substation 7
    s07m1 = net.addHost('s07m1', ip='100.7.0.11', cls=CPULimitedHost, cpu=.1)
    s07m2 = net.addHost('s07m2', ip='100.7.0.12', cls=CPULimitedHost, cpu=.1)
    s07m3 = net.addHost('s07m3', ip='100.7.0.13', cls=CPULimitedHost, cpu=.1)
    s07m4 = net.addHost('s07m4', ip='100.7.0.14', cls=CPULimitedHost, cpu=.1)
    s07m5 = net.addHost('s07m5', ip='100.7.0.15', cls=CPULimitedHost, cpu=.1)
    s07m6 = net.addHost('s07m6', ip='100.7.0.16', cls=CPULimitedHost, cpu=.1)
    s07m7 = net.addHost('s07m7', ip='100.7.0.17', cls=CPULimitedHost, cpu=.1)
    s07m8 = net.addHost('s07m8', ip='100.7.0.18', cls=CPULimitedHost, cpu=.1)
    s07m9 = net.addHost('s07m9', ip='100.7.0.19', cls=CPULimitedHost, cpu=.1)
    s07m10 = net.addHost('s07m10', ip='100.7.0.20', cls=CPULimitedHost, cpu=.1)
    s07cpc = net.addHost('s07cpc', ip='100.7.0.21')
    s07db = net.addHost('s07db', ip='100.7.0.22')
    s07gw = net.addHost('s07gw', ip='100.7.0.23')

    #Add Hosts on Substation 21
    s21m1 = net.addHost('s21m1', ip='100.21.0.11', cls=CPULimitedHost, cpu=.1)
    s21m2 = net.addHost('s21m2', ip='100.21.0.12', cls=CPULimitedHost, cpu=.1)
    s21m3 = net.addHost('s21m3', ip='100.21.0.13', cls=CPULimitedHost, cpu=.1)
    s21m4 = net.addHost('s21m4', ip='100.21.0.14', cls=CPULimitedHost, cpu=.1)
    s21m5 = net.addHost('s21m5', ip='100.21.0.15', cls=CPULimitedHost, cpu=.1)
    s21m6 = net.addHost('s21m6', ip='100.21.0.16', cls=CPULimitedHost, cpu=.1)
    s21cpc = net.addHost('s21cpc', ip='100.21.0.21')
    s21db = net.addHost('s21db', ip='100.21.0.22')
    s21gw = net.addHost('s21gw', ip='100.21.0.23')

    #Add Hosts on Substation 24
    s24m1 = net.addHost('s24m1', ip='100.24.0.11', cls=CPULimitedHost, cpu=.1)
    s24m2 = net.addHost('s24m2', ip='100.24.0.12', cls=CPULimitedHost, cpu=.1)
    s24m3 = net.addHost('s24m3', ip='100.24.0.13', cls=CPULimitedHost, cpu=.1)
    s24m4 = net.addHost('s24m4', ip='100.24.0.14', cls=CPULimitedHost, cpu=.1)
    s24m5 = net.addHost('s24m5', ip='100.24.0.15', cls=CPULimitedHost, cpu=.1)
    s24m6 = net.addHost('s24m6', ip='100.24.0.16', cls=CPULimitedHost, cpu=.1)
    s24cpc = net.addHost('s24cpc', ip='100.24.0.21')
    s24db = net.addHost('s24db', ip='100.24.0.22')
    s24gw = net.addHost('s24gw', ip='100.24.0.23')

    #Add Hosts on Substation 8
    s8m1 = net.addHost('s8m1', ip='100.8.0.11', cls=CPULimitedHost, cpu=.1)
    s8m2 = net.addHost('s8m2', ip='100.8.0.12', cls=CPULimitedHost, cpu=.1)
    s8m3 = net.addHost('s8m3', ip='100.8.0.13', cls=CPULimitedHost, cpu=.1)
    s8m4 = net.addHost('s8m4', ip='100.8.0.14', cls=CPULimitedHost, cpu=.1)
    s8m5 = net.addHost('s8m5', ip='100.8.0.15', cls=CPULimitedHost, cpu=.1)
    s8m6 = net.addHost('s8m6', ip='100.8.0.16', cls=CPULimitedHost, cpu=.1)
    s8cpc = net.addHost('s8cpc', ip='100.8.0.21')
    s8db = net.addHost('s8db', ip='100.8.0.22')
    s8gw = net.addHost('s8gw', ip='100.8.0.23')

    # Link switch to switch
    net.addLink(s51,s52)
    net.addLink(s53,s52)
    net.addLink(s61,s62)
    net.addLink(s63,s62)
    net.addLink(s71,s72)
    net.addLink(s73,s72)
    net.addLink(s211,s212)
    net.addLink(s213,s212)
    net.addLink(s241,s242)
    net.addLink(s243,s242)
    net.addLink(s81,s82)
    net.addLink(s83,s82)

    # Link Control Center to Switch
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'100.0.0.11/24'})
    net.addLink(cctl,s999, intfName1='cctl-eth1', params1={'ip':'100.0.0.12/24'})

    # Link Substation 5 Merging unit to Switch
    net.addLink(s05m1,s53, intfName1='s05m1-eth1', params1={'ip':'100.5.0.11/24'})
    net.addLink(s05m2,s53, intfName1='s05m2-eth1', params1={'ip':'100.5.0.12/24'})
    net.addLink(s05m3,s53, intfName1='s05m3-eth1', params1={'ip':'100.5.0.13/24'})
    net.addLink(s05m4,s53, intfName1='s05m4-eth1', params1={'ip':'100.5.0.14/24'})
    net.addLink(s05m5,s53, intfName1='s05m5-eth1', params1={'ip':'100.5.0.15/24'})
    net.addLink(s05m6,s53, intfName1='s05m6-eth1', params1={'ip':'100.5.0.16/24'}) 
    net.addLink(s05cpc,s52)
    net.addLink(s05db,s52)
    net.addLink(s05gw,s51, intfName1='s05gw-eth1', params1={'ip':'100.5.0.23/24'})

    # Link Substation 06 Merging unit to Switch
    net.addLink(s06m1, s63, intfName1='s06m1-eth1', params1={'ip': '100.6.0.11/24'})
    net.addLink(s06m2, s63, intfName1='s06m2-eth1', params1={'ip': '100.6.0.12/24'})
    net.addLink(s06m3, s63, intfName1='s06m3-eth1', params1={'ip': '100.6.0.13/24'})
    net.addLink(s06m4, s63, intfName1='s06m4-eth1', params1={'ip': '100.6.0.14/24'})
    net.addLink(s06m5, s63, intfName1='s06m5-eth1', params1={'ip': '100.6.0.15/24'})
    net.addLink(s06m6, s63, intfName1='s06m6-eth1', params1={'ip': '100.6.0.16/24'})
    net.addLink(s06m7, s63, intfName1='s06m7-eth1', params1={'ip': '100.6.0.17/24'})
    net.addLink(s06m8, s63, intfName1='s06m8-eth1', params1={'ip': '100.6.0.18/24'})
    net.addLink(s06m9, s63, intfName1='s06m9-eth1', params1={'ip': '100.6.0.19/24'})
    net.addLink(s06cpc, s62)
    net.addLink(s06db, s62)
    net.addLink(s06gw, s61, intfName1='s06gw-eth1', params1={'ip': '100.6.0.23/24'})

    # Link Substation 07 Merging unit to Switch
    net.addLink(s07m1, s73, intfName1='s07m1-eth1', params1={'ip': '100.7.0.11/24'})
    net.addLink(s07m2, s73, intfName1='s07m2-eth1', params1={'ip': '100.7.0.12/24'})
    net.addLink(s07m3, s73, intfName1='s07m3-eth1', params1={'ip': '100.7.0.13/24'})
    net.addLink(s07m4, s73, intfName1='s07m4-eth1', params1={'ip': '100.7.0.14/24'})
    net.addLink(s07m5, s73, intfName1='s07m5-eth1', params1={'ip': '100.7.0.15/24'})
    net.addLink(s07m6, s73, intfName1='s07m6-eth1', params1={'ip': '100.7.0.16/24'})
    net.addLink(s07m7, s73, intfName1='s07m7-eth1', params1={'ip': '100.7.0.17/24'})
    net.addLink(s07m8, s73, intfName1='s07m8-eth1', params1={'ip': '100.7.0.18/24'})
    net.addLink(s07m9, s73, intfName1='s07m9-eth1', params1={'ip': '100.7.0.19/24'})
    net.addLink(s07m10, s73, intfName1='s07m10-eth1', params1={'ip': '100.7.0.20/24'})
    net.addLink(s07cpc, s72)
    net.addLink(s07db, s72)
    net.addLink(s07gw, s71, intfName1='s07gw-eth1', params1={'ip': '100.7.0.23/24'})

    # Link Substation 21 Merging unit to Switch
    net.addLink(s21m1, s213, intfName1='s21m1-eth1', params1={'ip': '100.21.0.11/24'}, cls=TCLink, bw=0.01)
    net.addLink(s21m2, s213, intfName1='s21m2-eth1', params1={'ip': '100.21.0.12/24'}, cls=TCLink, bw=0.01)
    net.addLink(s21m3, s213, intfName1='s21m3-eth1', params1={'ip': '100.21.0.13/24'}, cls=TCLink, bw=0.01)
    net.addLink(s21m4, s213, intfName1='s21m4-eth1', params1={'ip': '100.21.0.14/24'}, cls=TCLink, bw=0.01)
    net.addLink(s21m5, s213, intfName1='s21m5-eth1', params1={'ip': '100.21.0.15/24'}, cls=TCLink, bw=0.01)
    net.addLink(s21m6, s213, intfName1='s21m6-eth1', params1={'ip': '100.21.0.16/24'}, cls=TCLink, bw=0.01)
    net.addLink(s21cpc, s212)
    net.addLink(s21db, s212)
    net.addLink(s21gw, s211, intfName1='s21gw-eth1', params1={'ip': '100.21.0.23/24'})

    # Link Substation 24 Merging unit to Switch
    net.addLink(s24m1,s243, intfName1='s24m1-eth1', params1={'ip':'100.24.0.11/24'})
    net.addLink(s24m2,s243, intfName1='s24m2-eth1', params1={'ip':'100.24.0.12/24'})
    net.addLink(s24m3,s243, intfName1='s24m3-eth1', params1={'ip':'100.24.0.13/24'})
    net.addLink(s24m4,s243, intfName1='s24m4-eth1', params1={'ip':'100.24.0.14/24'})
    net.addLink(s24m5,s243, intfName1='s24m5-eth1', params1={'ip':'100.24.0.15/24'})
    net.addLink(s24m6,s243, intfName1='s24m6-eth1', params1={'ip':'100.24.0.16/24'}) 
    net.addLink(s24cpc,s242)
    net.addLink(s24db,s242)
    net.addLink(s24gw,s241, intfName1='s24gw-eth1', params1={'ip':'100.24.0.23/24'})

    # Link Substation 25 Merging unit to Switch
    net.addLink(s8m1,s83, intfName1='s8m1-eth1', params1={'ip':'100.8.0.11/24'})
    net.addLink(s8m2,s83, intfName1='s8m2-eth1', params1={'ip':'100.8.0.12/24'})
    net.addLink(s8m3,s83, intfName1='s8m3-eth1', params1={'ip':'100.8.0.13/24'})
    net.addLink(s8m4,s83, intfName1='s8m4-eth1', params1={'ip':'100.8.0.14/24'})
    net.addLink(s8m5,s83, intfName1='s8m5-eth1', params1={'ip':'100.8.0.15/24'})
    net.addLink(s8m6,s83, intfName1='s8m6-eth1', params1={'ip':'100.8.0.16/24'}) 
    net.addLink(s8cpc,s82)
    net.addLink(s8db,s82)
    net.addLink(s8gw,s81, intfName1='s8gw-eth1', params1={'ip':'100.8.0.23/24'})

    # Link Host Control Center to getaway of substation 7
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.11/16'})
    net.addLink(cctl,s777, intfName1='cctl-eth0', params1={'ip':'10.0.0.12/16'})

    # Link Host Substation 5 to switch to gateway of substation 7
    net.addLink(s05m1,s777, intfName1='s05m1-eth0', params1={'ip':'10.0.5.11/16'})
    net.addLink(s05m2,s777, intfName1='s05m2-eth0', params1={'ip':'10.0.5.12/16'})
    net.addLink(s05m3,s777, intfName1='s05m3-eth0', params1={'ip':'10.0.5.13/16'})
    net.addLink(s05m4,s777, intfName1='s05m4-eth0', params1={'ip':'10.0.5.14/16'})
    net.addLink(s05m5,s777, intfName1='s05m5-eth0', params1={'ip':'10.0.5.15/16'})
    net.addLink(s05m6,s777, intfName1='s05m6-eth0', params1={'ip':'10.0.5.16/16'})
    net.addLink(s05gw,s777, intfName1='s05gw-eth0', params1={'ip':'10.0.5.23/16'})

    # Link Host Substation 6 to switch to getaway of substation 7
    net.addLink(s06m1, s777, intfName1='s06m1-eth0', params1={'ip': '10.0.6.11/16'})
    net.addLink(s06m2, s777, intfName1='s06m2-eth0', params1={'ip': '10.0.6.12/16'})
    net.addLink(s06m3, s777, intfName1='s06m3-eth0', params1={'ip': '10.0.6.13/16'})
    net.addLink(s06m4, s777, intfName1='s06m4-eth0', params1={'ip': '10.0.6.14/16'})
    net.addLink(s06m5, s777, intfName1='s06m5-eth0', params1={'ip': '10.0.6.15/16'})
    net.addLink(s06m6, s777, intfName1='s06m6-eth0', params1={'ip': '10.0.6.16/16'})
    net.addLink(s06m7, s777, intfName1='s06m7-eth0', params1={'ip': '10.0.6.17/16'})
    net.addLink(s06m8, s777, intfName1='s06m8-eth0', params1={'ip': '10.0.6.18/16'})
    net.addLink(s06m9, s777, intfName1='s06m9-eth0', params1={'ip': '10.0.6.19/16'})
    net.addLink(s06gw, s777, intfName1='s06gw-eth0', params1={'ip': '10.0.6.23/16'})

    # Link Host Substation 7 to switch to external gateway
    net.addLink(s07m1, s777, intfName1='s07m1-eth0', params1={'ip': '10.0.7.11/16'})
    net.addLink(s07m2, s777, intfName1='s07m2-eth0', params1={'ip': '10.0.7.12/16'})
    net.addLink(s07m3, s777, intfName1='s07m3-eth0', params1={'ip': '10.0.7.13/16'})
    net.addLink(s07m4, s777, intfName1='s07m4-eth0', params1={'ip': '10.0.7.14/16'})
    net.addLink(s07m5, s777, intfName1='s07m5-eth0', params1={'ip': '10.0.7.15/16'})
    net.addLink(s07m6, s777, intfName1='s07m6-eth0', params1={'ip': '10.0.7.16/16'})
    net.addLink(s07m7, s777, intfName1='s07m7-eth0', params1={'ip': '10.0.7.17/16'})
    net.addLink(s07m8, s777, intfName1='s07m8-eth0', params1={'ip': '10.0.7.18/16'})
    net.addLink(s07m9, s777, intfName1='s07m9-eth0', params1={'ip': '10.0.7.19/16'})
    net.addLink(s07m10, s777, intfName1='s07m10-eth0', params1={'ip': '10.0.7.20/16'})
    net.addLink(s07gw, s777, intfName1='s07gw-eth0', params1={'ip': '10.0.7.23/16'})

    # Link Host Substation 21 to switch to gateway of substation 7
    net.addLink(s21m1, s777, intfName1='s21m1-eth0', params1={'ip': '10.0.21.11/16'})
    net.addLink(s21m2, s777, intfName1='s21m2-eth0', params1={'ip': '10.0.21.12/16'})
    net.addLink(s21m3, s777, intfName1='s21m3-eth0', params1={'ip': '10.0.21.13/16'})
    net.addLink(s21m4, s777, intfName1='s21m4-eth0', params1={'ip': '10.0.21.14/16'})
    net.addLink(s21m5, s777, intfName1='s21m5-eth0', params1={'ip': '10.0.21.15/16'})
    net.addLink(s21m6, s777, intfName1='s21m6-eth0', params1={'ip': '10.0.21.16/16'})
    net.addLink(s21gw, s777, intfName1='s21gw-eth0', params1={'ip': '10.0.21.23/16'})

    # Link Host Substation 24 to switch to gateway of substation 7
    net.addLink(s24m1,s777, intfName1='s24m1-eth0', params1={'ip':'10.0.24.11/16'})
    net.addLink(s24m2,s777, intfName1='s24m2-eth0', params1={'ip':'10.0.24.12/16'})
    net.addLink(s24m3,s777, intfName1='s24m3-eth0', params1={'ip':'10.0.24.13/16'})
    net.addLink(s24m4,s777, intfName1='s24m4-eth0', params1={'ip':'10.0.24.14/16'})
    net.addLink(s24m5,s777, intfName1='s24m5-eth0', params1={'ip':'10.0.24.15/16'})
    net.addLink(s24m6,s777, intfName1='s24m6-eth0', params1={'ip':'10.0.24.16/16'})
    net.addLink(s24gw,s777, intfName1='s24gw-eth0', params1={'ip':'10.0.24.23/16'})

    
    # Link Host Substation 24 to switch to gateway of substation 7
    net.addLink(s8m1,s777, intfName1='s8m1-eth0', params1={'ip':'10.0.25.11/16'})
    """
    net.addLink(s8m2,s777, intfName1='s8m2-eth0', params1={'ip':'10.0.25.12/16'})
    net.addLink(s8m3,s777, intfName1='s8m3-eth0', params1={'ip':'10.0.25.13/16'})
    net.addLink(s8m4,s777, intfName1='s8m4-eth0', params1={'ip':'10.0.25.14/16'})
    net.addLink(s8m5,s777, intfName1='s8m5-eth0', params1={'ip':'10.0.25.15/16'})
    net.addLink(s8m6,s777, intfName1='s8m6-eth0', params1={'ip':'10.0.25.16/16'})
    net.addLink(s8gw,s777, intfName1='s8gw-eth0', params1={'ip':'10.0.25.23/16'})
    """


    #Build and start Network ============================================================================
    net.build()
    net.addNAT(ip='10.0.0.250').configDefault()
    net.start()

    #Configure GRE Tunnel
    #s777.cmdPrint('ovs-vsctl add-port s777 s777-gre1 -- set interface s777-gre1 type=gre ofport_request=5 options:remote_ip='+NODE2_IP)
    #s777.cmdPrint('ovs-vsctl show')
    nat = net.get('nat0')
    nat.cmdPrint('ip link set mtu 1454 dev nat0-eth0')

    # Add routing for reaching networks that aren't directly connected
    info( net[ 'r0' ].cmd( 'ip route add 100.5.0.0/24 via 200.5.0.2 dev r0-eth2' ) )
    info( net[ 'r5' ].cmd( 'ip route add 100.0.0.0/24 via 200.5.0.1 dev r5-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.6.0.0/24 via 200.6.0.2 dev r0-eth3' ) )
    info( net[ 'r6' ].cmd( 'ip route add 100.0.0.0/24 via 200.6.0.1 dev r6-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.7.0.0/24 via 200.7.0.2 dev r0-eth4' ) )
    info( net[ 'r7' ].cmd( 'ip route add 100.0.0.0/24 via 200.7.0.1 dev r7-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.21.0.0/24 via 200.21.0.2 dev r0-eth5' ) )
    info( net[ 'r21' ].cmd( 'ip route add 100.0.0.0/24 via 200.21.0.1 dev r21-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.24.0.0/24 via 200.24.0.2 dev r0-eth6' ) )
    info( net[ 'r24' ].cmd( 'ip route add 100.0.0.0/24 via 200.24.0.1 dev r24-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.8.0.0/24 via 200.8.0.2 dev r0-eth7' ) )
    info( net[ 'r8' ].cmd( 'ip route add 100.0.0.0/24 via 200.8.0.1 dev r8-eth2' ) )

    info( net[ 's05m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m1-eth1' ) )
    info( net[ 's05m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m2-eth1' ) )
    info( net[ 's05m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m3-eth1' ) )
    info( net[ 's05m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m4-eth1' ) )
    info( net[ 's05m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m5-eth1' ) )
    info( net[ 's05m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.5.0.1 dev s05m6-eth1' ) )

    info( net[ 's05m1' ].cmd( 'ip route add 200.0.0.0/8 via 100.5.0.1 dev s05m1-eth1' ) )
    info( net[ 's05m2' ].cmd( 'ip route add 200.0.0.0/8 via 100.5.0.1 dev s05m2-eth1' ) )
    info( net[ 's05m3' ].cmd( 'ip route add 200.0.0.0/8 via 100.5.0.1 dev s05m3-eth1' ) )
    info( net[ 's05m4' ].cmd( 'ip route add 200.0.0.0/8 via 100.5.0.1 dev s05m4-eth1' ) )
    info( net[ 's05m5' ].cmd( 'ip route add 200.0.0.0/8 via 100.5.0.1 dev s05m5-eth1' ) )
    info( net[ 's05m6' ].cmd( 'ip route add 200.0.0.0/8 via 100.5.0.1 dev s05m6-eth1' ) )

    info( net['s06m1'].cmd('ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m1-eth1'))
    info( net['s06m2'].cmd('ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m2-eth1'))
    info( net['s06m3'].cmd('ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m3-eth1'))
    info( net['s06m4'].cmd('ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m4-eth1'))
    info( net['s06m5'].cmd('ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m5-eth1'))
    info( net['s06m6'].cmd('ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m6-eth1'))
    info( net['s06m7'].cmd('ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m7-eth1'))
    info( net['s06m8'].cmd('ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m8-eth1'))
    info( net['s06m9'].cmd('ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m9-eth1'))

    info( net['s06m1'].cmd('ip route add 200.0.0.0/8 via 100.6.0.1 dev s06m1-eth1'))
    info( net['s06m2'].cmd('ip route add 200.0.0.0/8 via 100.6.0.1 dev s06m2-eth1'))
    info( net['s06m3'].cmd('ip route add 200.0.0.0/8 via 100.6.0.1 dev s06m3-eth1'))
    info( net['s06m4'].cmd('ip route add 200.0.0.0/8 via 100.6.0.1 dev s06m4-eth1'))
    info( net['s06m5'].cmd('ip route add 200.0.0.0/8 via 100.6.0.1 dev s06m5-eth1'))
    info( net['s06m6'].cmd('ip route add 200.0.0.0/8 via 100.6.0.1 dev s06m6-eth1'))
    info( net['s06m7'].cmd('ip route add 200.0.0.0/8 via 100.6.0.1 dev s06m7-eth1'))
    info( net['s06m8'].cmd('ip route add 200.0.0.0/8 via 100.6.0.1 dev s06m8-eth1'))
    info( net['s06m9'].cmd('ip route add 200.0.0.0/8 via 100.6.0.1 dev s06m9-eth1'))

    info(net['s07m1'].cmd('ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m1-eth1'))
    info(net['s07m2'].cmd('ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m2-eth1'))
    info(net['s07m3'].cmd('ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m3-eth1'))
    info(net['s07m4'].cmd('ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m4-eth1'))
    info(net['s07m5'].cmd('ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m5-eth1'))
    info(net['s07m6'].cmd('ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m6-eth1'))
    info(net['s07m7'].cmd('ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m7-eth1'))
    info(net['s07m8'].cmd('ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m8-eth1'))
    info(net['s07m9'].cmd('ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m9-eth1'))

    info(net['s07m1'].cmd('ip route add 200.0.0.0/8 via 100.7.0.1 dev s07m1-eth1'))
    info(net['s07m2'].cmd('ip route add 200.0.0.0/8 via 100.7.0.1 dev s07m2-eth1'))
    info(net['s07m3'].cmd('ip route add 200.0.0.0/8 via 100.7.0.1 dev s07m3-eth1'))
    info(net['s07m4'].cmd('ip route add 200.0.0.0/8 via 100.7.0.1 dev s07m4-eth1'))
    info(net['s07m5'].cmd('ip route add 200.0.0.0/8 via 100.7.0.1 dev s07m5-eth1'))
    info(net['s07m6'].cmd('ip route add 200.0.0.0/8 via 100.7.0.1 dev s07m6-eth1'))
    info(net['s07m7'].cmd('ip route add 200.0.0.0/8 via 100.7.0.1 dev s07m7-eth1'))
    info(net['s07m8'].cmd('ip route add 200.0.0.0/8 via 100.7.0.1 dev s07m8-eth1'))
    info(net['s07m9'].cmd('ip route add 200.0.0.0/8 via 100.7.0.1 dev s07m9-eth1'))

    info(net['s21m1'].cmd('ip route add 100.0.0.0/24 via 100.21.0.1 dev s21m1-eth1'))
    info(net['s21m2'].cmd('ip route add 100.0.0.0/24 via 100.21.0.1 dev s21m2-eth1'))
    info(net['s21m3'].cmd('ip route add 100.0.0.0/24 via 100.21.0.1 dev s21m3-eth1'))
    info(net['s21m4'].cmd('ip route add 100.0.0.0/24 via 100.21.0.1 dev s21m4-eth1'))
    info(net['s21m5'].cmd('ip route add 100.0.0.0/24 via 100.21.0.1 dev s21m5-eth1'))
    info(net['s21m6'].cmd('ip route add 100.0.0.0/24 via 100.21.0.1 dev s21m6-eth1'))

    info(net['s21m1'].cmd('ip route add 200.0.0.0/8 via 100.21.0.1 dev s21m1-eth1'))
    info(net['s21m2'].cmd('ip route add 200.0.0.0/8 via 100.21.0.1 dev s21m2-eth1'))
    info(net['s21m3'].cmd('ip route add 200.0.0.0/8 via 100.21.0.1 dev s21m3-eth1'))
    info(net['s21m4'].cmd('ip route add 200.0.0.0/8 via 100.21.0.1 dev s21m4-eth1'))
    info(net['s21m5'].cmd('ip route add 200.0.0.0/8 via 100.21.0.1 dev s21m5-eth1'))
    info(net['s21m6'].cmd('ip route add 200.0.0.0/8 via 100.21.0.1 dev s21m6-eth1'))

    info( net[ 's24m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m1-eth1' ) )
    info( net[ 's24m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m2-eth1' ) )
    info( net[ 's24m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m3-eth1' ) )
    info( net[ 's24m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m4-eth1' ) )
    info( net[ 's24m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m5-eth1' ) )
    info( net[ 's24m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.24.0.1 dev s24m6-eth1' ) )

    info( net[ 's24m1' ].cmd( 'ip route add 200.0.0.0/8 via 100.24.0.1 dev s24m1-eth1' ) )
    info( net[ 's24m2' ].cmd( 'ip route add 200.0.0.0/8 via 100.24.0.1 dev s24m2-eth1' ) )
    info( net[ 's24m3' ].cmd( 'ip route add 200.0.0.0/8 via 100.24.0.1 dev s24m3-eth1' ) )
    info( net[ 's24m4' ].cmd( 'ip route add 200.0.0.0/8 via 100.24.0.1 dev s24m4-eth1' ) )
    info( net[ 's24m5' ].cmd( 'ip route add 200.0.0.0/8 via 100.24.0.1 dev s24m5-eth1' ) )
    info( net[ 's24m6' ].cmd( 'ip route add 200.0.0.0/8 via 100.24.0.1 dev s24m6-eth1' ) )

    info( net[ 's8m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s8m1-eth1' ) )
    info( net[ 's8m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s8m2-eth1' ) )
    info( net[ 's8m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s8m3-eth1' ) )
    info( net[ 's8m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s8m4-eth1' ) )
    info( net[ 's8m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s8m5-eth1' ) )
    info( net[ 's8m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s8m6-eth1' ) )

    info( net[ 's8m1' ].cmd( 'ip route add 200.0.0.0/8 via 100.8.0.1 dev s8m1-eth1' ) )
    info( net[ 's8m2' ].cmd( 'ip route add 200.0.0.0/8 via 100.8.0.1 dev s8m2-eth1' ) )
    info( net[ 's8m3' ].cmd( 'ip route add 200.0.0.0/8 via 100.8.0.1 dev s8m3-eth1' ) )
    info( net[ 's8m4' ].cmd( 'ip route add 200.0.0.0/8 via 100.8.0.1 dev s8m4-eth1' ) )
    info( net[ 's8m5' ].cmd( 'ip route add 200.0.0.0/8 via 100.8.0.1 dev s8m5-eth1' ) )
    info( net[ 's8m6' ].cmd( 'ip route add 200.0.0.0/8 via 100.8.0.1 dev s8m6-eth1' ) )
    
    info( net[ 'ccdb' ].cmd( 'ip route add 100.5.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.6.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.7.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.21.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.24.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.25.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )

    info( net[ 'cctl' ].cmd( 'ip route add 100.5.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.6.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.7.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.21.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.25.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    
    info(os.system('ip addr add 100.0.0.99/24 dev s999'))
    info(os.system('ip link set s999 up'))

    time.sleep(2)

    """

    

    info( net[ 's05m1' ].cmd( 'python3.6 as05m1.py &amp' ) )
    info( net[ 's05m2' ].cmd( 'python3.6 as05m2.py &amp' ) )
    info( net[ 's05m3' ].cmd( 'python3.6 as05m3.py &amp' ) )

    

    info(net['s06m1'].cmd('python3.6 as06m1.py &amp'))
    info(net['s06m2'].cmd('python3.6 as06m2.py &amp'))
    info(net['s06m3'].cmd('python3.6 as06m3.py &amp'))
    info(net['s06m4'].cmd('python3.6 as06m4.py &amp'))
    info(net['s06m5'].cmd('python3.6 as06m5.py &amp'))
    info(net['s06m6'].cmd('python3.6 as06m6.py &amp'))

    info(net['s07m1'].cmd('python3.6 as07m1.py &amp'))
    info(net['s07m2'].cmd('python3.6 as07m2.py &amp'))
    info(net['s07m3'].cmd('python3.6 as07m3.py &amp'))
    info(net['s07m4'].cmd('python3.6 as07m4.py &amp'))
    info(net['s07m5'].cmd('python3.6 as07m5.py &amp'))
    info(net['s07m6'].cmd('python3.6 as07m6.py &amp'))
    info(net['s07m7'].cmd('python3.6 as07m7.py &amp'))
    info(net['s07m8'].cmd('python3.6 as07m8.py &amp'))
    info(net['s07m9'].cmd('python3.6 as07m9.py &amp'))
    info(net['s07m10'].cmd('python3.6 as07m10.py &amp'))

    info(net['s21m1'].cmd('python3.6 as21m1.py &amp'))
    info(net['s21m2'].cmd('python3.6 as21m2.py &amp'))
    info(net['s21m3'].cmd('python3.6 as21m3.py &amp'))

    info( net[ 's24m1' ].cmd( 'python3.6 as24m1.py &amp' ) )
    info( net[ 's24m2' ].cmd( 'python3.6 as24m2.py &amp' ) )
    info( net[ 's24m3' ].cmd( 'python3.6 as24m3.py &amp' ) )
    info( net[ 's24m4' ].cmd( 'python3.6 as24m4.py &amp' ) )
    info( net[ 's24m5' ].cmd( 'python3.6 as24m5.py &amp' ) )
    info( net[ 's24m6' ].cmd( 'python3.6 as24m6.py &amp' ) )

    time.sleep(2)

    info( net[ 'ccdb' ].cmd( 'python3.6 as05gdb.py &amp' ) )
    info( net[ 'ccdb' ].cmd( 'python3.6 as06gdb.py &amp' ) )
    info( net[ 'ccdb' ].cmd( 'python3.6 as07gdb.py &amp' ) )
    info( net[ 'ccdb' ].cmd( 'python3.6 as21gdb.py &amp' ) )
    info( net[ 'ccdb' ].cmd( 'python3.6 as24gdb.py &amp' ) )

    """

    """

    time.sleep(2)

    info( net[ 's05m1' ].cmd( 'python3.6 as05gcc.py &amp' ) )
    info( net[ 's06m1' ].cmd( 'python3.6 as06gcc.py &amp' ) )
    info( net[ 's07m1' ].cmd( 'python3.6 as07gcc.py &amp' ) )
    info( net[ 's21m1' ].cmd( 'python3.6 as21gcc.py &amp' ) )
    info( net[ 's24m1' ].cmd( 'python3.6 as24gcc.py &amp' ) )

    """

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()