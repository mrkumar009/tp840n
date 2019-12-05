import re
from funct import *


def main():
    url = input("URL or Enter: ") or "http://192.168.0.1/cgi?6"
    sel_prim = input("1. Monitor Data Rates\n\
                      2. Set Alarm\n\
                      3. Display Details\n")
    if sel_prim == None:
        print("Select an option...")
    elif sel_prim == "1":
        monitor_rates
    elif sel_prim == "2":
        set_alarm
    elif sel_prim == "3":
        disp_detail(url)


main()
