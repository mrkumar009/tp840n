import os
import sys
import time
from data import *


def disp_detail(url):
    while True:
        try:
            raw_data = get_data(url)
            mac_addr, pkt_nos = list_data(raw_data)
            os.system('cls' if os.name=='nt' else 'clear')
            #print(chr(27) + "[2J")
            #for i, mac_addr, pkt_nos in enumerate(mac_addr, start=1):
            #    print("{0}. {1}     {2}".format(i, mac_addr, convert_size(pkt_to_byte(pkt_nos))))
            zipped = zip(mac_addr, pkt_nos)
            for it in zipped:
                iter(it)
                print("{0}  {1}".format(it[0], convert_size(pkt_to_byte(it[1]))))

            time.sleep(5)
        except KeyboardInterrupt:
            print("Exiting...")
            raise


