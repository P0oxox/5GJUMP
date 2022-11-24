import os
import sys
import time
import json
from json import load
import sys
import logging
import subprocess 
from ping3 import ping, verbose_ping
from datetime import datetime
import threading



    #         if a["fo"]["main_iface"] not in :
    #             os.system('ifmetric {0} 1'.format(a["fo"]["main_iface"]))
    #             os.system('ifmetric {0} 2'.format(a["fo"]["sec_iface"]))
    #             os.system('ifmetric {0} 3'.format(a["fo"]["backup_iface"]))
    #             for i in range(len(no_use)):
    #                 os.system('ifmetric {0} {1}'.format(no_use[i],i+10))
                
    #             os.system('iptables -t nat -D POSTROUTING -s {0} -o {1} -j MASQUERADE'.format('192.168.0.0/24',a["fo"]["sec_iface"]))
    #             os.system('iptables -t nat -D POSTROUTING -s {0} -o {1} -j MASQUERADE'.format('192.168.0.0/24',a["fo"]["backup_iface"]))
    #             nat_show = subprocess.getoutput("iptables -t nat -v -L POSTROUTING -n --line-number")
    #             if a["fo"]["main_iface"] not in nat_show:
    #                 os.system('iptables -t nat -A POSTROUTING -s {0} -o {1} -j MASQUERADE'.format('192.168.0.0/24',a["fo"]["main_iface"]))


if __name__ == '__main__':
    ifaces = ['usb0','wlan0']
    ifmetric_show = subprocess.getoutput("route -n")
    line_list = ifmetric_show.split('\n')
    print(line_list[2])

