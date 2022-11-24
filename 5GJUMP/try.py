import os
import sys
import time
import json
from json import load
import sys
import logging
import subprocess 
from ping3 import ping, verbose_ping

def setting():
    if_info = sys.argv[1]
    str_2_dic = json.loads(if_info)

    output_json1 = {"mode":str_2_dic["mode"],"ping_target":str_2_dic["ping_target"]}
    output_json2 = {}
    if str_2_dic["mode"]=="fo":    
        output_json2["fo"] = {"failback": str_2_dic["failback"],"main_iface":str_2_dic["main_iface"],"sec_iface":str_2_dic["sec_iface"],"backup_iface":str_2_dic["backup_iface"],"detection_mode":str_2_dic["detection_mode"] }
        output_json2["fo"]["latency"] = {"threshold":str_2_dic["latency"]["threshold"],"detection_period":str_2_dic["latency"]["detection_period"]}       
    output_json3 = {}
    if str_2_dic["mode"]=="single":  
        output_json3["single"] = {"main_iface": str_2_dic["main_wan"]}
    
    output_json1.update(output_json2)
    output_json1.update(output_json3)
    return output_json1

if __name__ == '__main__':
    setting()
