import funct


def main():
    funct.cls()
    sel_prim = input("\
            Welcome to tp840n:\n\
            1. Monitor Data Rates\n\
            2. Set Alarm\n\
            3. Display Details\n\n:")
    if sel_prim == "":
        print("Select an option...")
    elif sel_prim == "1":
        funct.test()
    elif sel_prim == "2":
        funct.test()
    elif sel_prim == "3":
        funct.disp_detail()


if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
       print("\n\rExiting...")
       pass
