from funct import *


def main():
    cls()
    sel = input('1. Display Used Data\r\n2. Display Data Rate\r\nSelect: ')
    if sel == '1':
        disp_detail()
    elif sel == '2':
        monitor_rates()


if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
       print("\n\rExiting...")
       pass
