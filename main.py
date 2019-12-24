from funct import *


def main():
    sel = input(': ')
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
