from data import *
from funct import *


def main():
    cls()
    url = input("URL or Enter: ") or "http://192.168.0.1/cgi?6"
    cls()
    sel_prim = input("\
            Welcome to tp840n:\n\
            1. Monitor Data Rates\n\
            2. Set Alarm\n\
            3. Display Details\n\n:")
    if sel_prim == "":
        print("Select an option...")
    elif sel_prim == "1":
        monitor_rates
    elif sel_prim == "2":
        set_alarm
    elif sel_prim == "3":
        disp_detail(url)


if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
       print("\n\rExiting...")
       pass
