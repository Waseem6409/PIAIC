while True:
            while True:
                        try:
                            hours = int(input("\nInput hours: ")) * 3600
                            minutes = int(input("\nInput minutes: ")) * 60
                            seconds = int(input("\nInput seconds: "))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            all_sec=(hours+minutes+seconds)
            print("\nThe amount of seconds is %d seconds." % all_sec)
            while True:
                        Repeat=input("\nDo you want to calculate again?\n\nYes or No:")
                        Repeat=Repeat.lower()
                        if Repeat not in ["yes","y","no","n"]:
                            print("\nPlease select correct option")
                        else:
                            break
                        
                            
            if Repeat in ["yes","y"]:
                continue
            else:
                if Repeat in ["no","n"]:
                    print("\n-----Thank you for using-----")
                    input()
                    break