import os
from data import *


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def disp_detail():
    cls()
    print('Wait... Connecting... ')
    while True:
        try:
            raw_data = get_data()
            mac_addr, pkts_nos = list_data(raw_data)
            cls()
            fmt = '{:<4}{:<22}{:<15}{:<15}'
            print(fmt.format('No', 'Mac Address', 'Recieved Data', 'Sent Data'))
            for i, (mac_addr, pkts_nos_rcd, pkts_nos_snd) in enumerate(zip(mac_addr, pkts_nos[1::2], pkts_nos[0::2]), start=1):
                print(fmt.format(i, mac_addr, convert_pkt(pkts_nos_rcd), convert_pkt(pkts_nos_snd)))
            time.sleep(5)
        except KeyboardInterrupt:
            raise


def monitor_rates():
    cls()
    print('Wait... Connecting... ')
    while True:
        try:
            raw_data = get_data()
            mac_addr, pkts_nos_prv = list_data(raw_data)
            time.sleep(5)
            cls()
            raw_data = get_data()
            mac_addr, pkts_nos = list_data(raw_data)
            fmt = '{:<6}{:<30}{:<20}{:<20}{:<20}{:<20}'
            print(fmt.format('No', 'Mac Address', 'Recieved Data', 'Sent Data', 'Rcd Data Rate', 'Sent Data Rate'))
            for i, (mac_addr, pkts_nos_rcd, pkts_nos_snd, pkts_nos_rcd_prv, pkts_nos_snd_prv) in enumerate(zip(mac_addr, pkts_nos[1::2], pkts_nos[0::2], pkts_nos_prv[1::2], pkts_nos_prv[0::2]), start=1):
                print(fmt.format(i, mac_addr, convert_pkt(pkts_nos_rcd), convert_pkt(pkts_nos_snd), convert_pkt(int(int(pkts_nos_rcd) - int(pkts_nos_rcd_prv)) // 5), convert_pkt(int(int(pkts_nos_snd) - int(pkts_nos_snd_prv)) // 5)))


        except KeyboardInterrupt:
            raise
