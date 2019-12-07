import os
import sys
import time
from data import *


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def disp_detail(url):
    while True:
        raw_data = get_data(url)
        mac_addr, pkts_nos = list_data(raw_data)
        cls()
        pkts_nos_rcd = []
        pkts_nos_snd = []
        for rcd in pkts_nos[1::2]:
            pkts_nos_rcd.append(rcd)
        for snd in pkts_nos[0::2]:
            pkts_nos_snd.append(snd)
        fmt = '{:<4}{:<22}{:<15}{:<15}'
        print(fmt.format('No', 'Mac Address', 'Recieved Data', 'Sent Data'))
        for i, (mac_addr, pkts_nos_rcd, pkts_nos_snd) in enumerate(zip(mac_addr, pkts_nos_rcd, pkts_nos_snd), start=1):
            print(fmt.format(i, mac_addr, convert_pkt(pkts_nos_rcd), convert_pkt(pkts_nos_snd)))
        time.sleep(5)


