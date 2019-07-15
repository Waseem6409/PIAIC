while True:
        while True:
                    try:
                        base = float(input('\nEnter base of triangle:'))
                    except ValueError:
                        print("\nPlease enter only number")
                    else:
                        break
        while True:
                    try:
                        height = float(input('\nEnter height of triangle:'))
                    except ValueError:
                        print("\nPlease enter only number")
                    else:
                        break
        vol_of_tri=(1.0/2.0)*(height*base)
        print("\nThe volume of triangle is",vol_of_tri,'.')
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